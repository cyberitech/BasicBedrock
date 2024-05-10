"""
Basic Bedrock Python API abstraction.
Currently supports all text-modal foundation models in AWS Bedrock.
Abstracts away the need to understand any of the model-specific response or request semantics.
Simply pick a model, and invoke it with a prompt.
If you with to specify k, p, temp, and max_token parameters, they will be applied on a best effort basis.
not all models support all parameters.
"""

import json
import warnings

import boto3
import pydantic

from models import *
from basicbedrock.guardrails import Guardrails


class BasicBedrock(object):
    def __init__(self, session: boto3.session.Session = None, **kwargs):
        """
        Creates an instance of basic bedrock.
        session param is optional.  If omitted, a default session constructor will be used.
        Right now, the only kwargs supported are a param dictionary.
        Param dicts are in the format of {'top_p': float, 'top_k': int, 'temp': float, 'max_tokens': int}
        :param session: the boto3 session to use for creating the basic bedrock instance
        :param kwargs: kwargs used are in the format of {'top_p': float, 'top_k': int, 'temp': float, 'max_tokens': int}
        """
        if not session:
            #warnings.warn('No session provided, attempting to use "default" profile', category=RuntimeWarning)
            session = boto3.session.Session()
        self.client = session.client("bedrock-runtime")
        self._default_k = 100
        self._default_p = .5
        self._default_t = .5
        self._default_n = 150
        self._default_stop = []
        # intialize params to default values
        self._k = self._default_k
        self._p = self._default_p
        self._t = self._default_t
        self._n = self._default_n
        self._s = self._default_stop
        # set params according to kwargs
        if kwargs:
            self.set_params(kwargs)

        # We need to know what models are enabled in the aws account for this region
        _bedrock_cp = session.client("bedrock")
        r = _bedrock_cp.list_foundation_models()
        self.enabled_models = [
            e.get('modelId') for e in r['modelSummaries'] if e.get('modelLifecycle').get('status') == 'ACTIVE'
        ]
        self.available_models = sorted(  # calculates and sorts nodels both enabled and supported
            list(
                set(
                    self.enabled_models
                ).intersection(
                    set(
                        BasicBedrock.get_supported_models()
                    )
                )
            )
        )

    def print_available_models(self):
        """
        Prints available models that are supported by BasicBedrock and enabled in the aws account
        :return:
        """
        print(os.linesep.join(self.available_models))

    def get_available_models(self):
        """
        Gets a list of available models that are supported by BasicBedrock and enabled in the aws account
        :return: list of models both enabled and suported
        """
        return self.available_models

    @staticmethod
    def print_supported_models() -> None:
        """
        Prints all models supported by BasicBedrock, which may not be the same models a user has enabled within their account
        :return: None
        """
        print(os.linesep.join(BasicBedrock.get_supported_models()))

    @staticmethod
    def get_supported_models() -> list:
        """
        returns a list of all models supported by BasicBedrock, which may not be the same models a user has enabled within their account
        :return: ["model1", "model2", "model3"...]
        """
        return sorted(model_request_mapping.keys())

    @staticmethod
    def get_model_schema_dict(self, model_id: str) -> dict:
        """
        returns a dict object representing the request scheme of model_id
        :param model_id:  the chosen model id
        :return: dict object representing the base request scheme of model_id
        """
        if model_id not in BasicBedrock.get_supported_models():
            raise ValueError(f"requested model {model_id} is not an available model")
        else:
            model = model_request_mapping.get(model_id)
            _inst = model()
            j = _inst.json()
            d = json.loads(j)
            return d

    @staticmethod
    def get_model_request_object(model_id: str) -> BaseAbstractRequest:
        """
        returns an instantiated object representing the schema for the chosen model.
        All these inherit from BaseSchemaAbstract.
        Its useful for when you want to use BaseSchemaAbstract to modify prompts and produce json or dicts manually
        :param model_id: the chosen model ID
        :return: the schema class object for the chosen model, it will be a subclass of a BaseAbstractRequest
        """
        if model_id not in BasicBedrock.get_supported_models():
            raise ValueError(f"requested model {model_id} is not an available model in BasicBedrock")
        _inst = model_request_mapping.get(model_id)()
        return _inst

    @staticmethod
    def get_model_request_json(model_id: str) -> str:
        """
        returns a string object representing the request scheme of model_id in json format
        :param model_id:  the chosen model id
        :return: a json string
        """
        if model_id not in BasicBedrock.get_supported_models():
            raise ValueError(f"requested model {model_id} is not an available model in BasicBedrock")
        else:
            model = model_request_mapping.get(model_id)
            _inst = model()
            j = _inst.json()
            return j


    @staticmethod
    def print_model_schema(model_id: str, indent: int = None) -> None:
        """
        prints the request scheme of model_id in a pretty format.
        if indent is not None, indent the lines when printing
        :param model_id: the chosen model id
        :param indent: how many spaces to indent, default=4
        :return: None
        """
        if model_id not in BasicBedrock.get_supported_models():
            raise ValueError(f"requested model {model_id} is not an available model in BasicBedrock")
        else:
            model = model_request_mapping.get(model_id)
            _inst = model()
            j = _inst.json()
            if indent:
                j = json.dumps(json.loads(j), indent=indent)
        print(j)

    def get_boto3_body(self, model_id: str, prompt: str) -> str:
        """
        given a model_id and a prompt, this will construct the boto3 'body' parameter using the specified prompt and params,
        but it will not invoke bedrock or pass it to boto3, it will simply return the boto3 'body' param as a string.
        Internally, this calls the update_prompt() function, not update_prompt_raw(), which means that it will take into account
        the expected calling convention of the underlying model by inserting things such as 'Human:' or '<s>[INST]' as appropriate
        :param model_id: the model to construct a boto3 body for
        :param prompt: the prompt to pass the model.
        :return: a string, representing the equivalent boto3 'body' parameter.
        """
        if model_id not in BasicBedrock.get_supported_models():
            raise ValueError(f"requested model {model_id} is not an available model in BasicBedrock")
        if not isinstance(prompt, str):
            raise ValueError(f"prompt must be a string, but got {type(prompt)}")
        schema = model_request_mapping.get(model_id)
        schema_inst: BaseAbstractRequest = schema()
        schema_inst.set_prompt(prompt)
        schema_inst.set_params(self.params)
        j = schema_inst.json()
        return j

    def invoke(self, model_id: str, request: typing.Union[str, dict],
              show_request: bool = False, guardrail: Guardrails = None) -> BaseAbstractResponse:
        """
        invokes a model_id and returns the response.  Non-streaming only.
        request may by one of: a prompt, a json string represent the request schema, or a dict representing the request schema
        invoking with a request of a string containing valid json data, if it is not a valid json schema for the model
        it will be interpreted as a prompt string and a runtime warning will be raised
        :param model_id: the model id you wish to invoke
        :param request: a string or dict representing either a prompt or a model request schema
        :param: guardrail: Optional instance of a basicbedrock.guardrails.Guardrails class. If present, it will utilize the guardrail within it.
        :param show_request: prints the request blob before invoking
        :return: the response to the request, as a subclass of a model.BaseAbstractResponse
        """
        if model_id not in BasicBedrock.get_supported_models():
            raise ValueError(f"requested model {model_id} is not an available model in BasicBedrock")
        if not isinstance(request, dict) and not isinstance(request, str):
            raise TypeError(f"request must be a string, or a json dict representing the request schema for the model, "
                            f"found: {type(request)}")
        schema_obj: BaseAbstractRequest = model_request_mapping.get(model_id)
        if schema_obj is None:
            raise ValueError(f"requested model {model_id} is not an available model")
        if guardrail is not None and not isinstance(guardrail, Guardrails):
            raise ValueError(f"object provided for guardrail parameter is a {type(guardrail)} but expected is a Guardrail or None")
        if guardrail is not None:
            if not guardrail.content_configuration and not guardrail.topic_configuration:
                warnings.warn(f"Empty guardrails provided for invoking model {model_id}, ignoring it")
                guardrail = None
            if not guardrail.guardrail_id:
                warnings.warn(f"Passed a guardrail to invoke() but guardrails not yet installed.  "
                              f"Installing now (remember to call uninstall_guardrails() afterwards to remove the guardrail from your account")
                guardrail.install_guardrails()
        schema_inst = None
        if isinstance(request, dict):
            # infer if the request is valid
            try:
                schema_inst = schema_obj.parse_obj(request)
            except pydantic.ValidationError:
                schema_inst = schema_obj()
                valid_j = schema_inst.json()
                invalid_j = json.dumps(request)
                raise ValueError(
                    f"inavlid request dict was provided for {model_id}.. wanted: {valid_j} but received: {invalid_j}")
        elif isinstance(request, str):
            try:
                j_load = json.loads(request)
                try:
                    schema_inst = schema_obj.parse_obj(j_load)
                except pydantic.ValidationError:  # it is json, but not an encoded json representing the model schema
                    warnings.warn(
                        f"received a well-formatted json string, but it was not the style except for the body "
                        f"parameter.  interpreting it as a string prompt rather than a marshalled request body",
                        category=Warning
                    )
                    sys.stderr.flush()
            except json.decoder.JSONDecodeError:  # its not marshalled json, its a string
                pass
        if schema_inst is None:
            schema_inst = schema_obj()
            schema_inst.set_prompt(request)
        schema_inst.set_params(self.params)
        body = schema_inst.json()
        full_request = {
            "modelId": model_id,
            "body": body
        }
        if guardrail is not None:
            full_request.update({
                "guardrailIdentifier": guardrail.guardrail_id,
                "guardrailVersion": guardrail.guardrail_version,
            })
        if show_request:
            print(json.dumps(full_request))
        r = self.client.invoke_model(**full_request)
        if r['ResponseMetadata']['HTTPStatusCode'] != 200:
            error = r.get('Error')
            code = error.get('Code')
            message = error.get('Message')
            raise RuntimeError(
                f"Encountered a non-200 status code {r['ResponseMetadata']['HTTPStatusCode']}, Code: {code}, Message: {message}")
        resp_body = r.get('body')
        resp_body = resp_body.read()
        resp_body = json.loads(resp_body)

        response_obj = model_response_mapping.get(model_id)
        response_inst = response_obj(res=resp_body)
        return response_inst

    def set_params(self, params: dict) -> None:
        """
        wrapper for property params, allow you to call it as a function
        :param params: a dict containing any of top_p, top_k, temp, max_tokens
        :return:
        """
        self.params = params

    def reset_params(self):
        """
        resets the params dictionary to default values
        these values are defined in _default_k, _default_p, _default_t, _default_n
        :return:
        """
        del self.params

    @property
    def params(self) -> dict:
        """
        returns the params dictionary
        :return: params dict in format of {'top_p': float, 'top_k': int, 'temp': float, 'max_tokens': int}
        """
        return {
            "top_p": self._p,
            "top_k": self._k,
            "temp": self._t,
            "max_tokens": self._n,
            "stop_words": self._s
        }

    @params.setter
    def params(self, params: dict):
        """
        applys a provided params dict to internal params
        :param params:
        :return:
        """
        if not isinstance(params, dict):
            raise ValueError(f"params must be a dict, not a {type(params)}")
        if "top_p" not in params and \
                "top_k" not in params and \
                "max_tokens" not in params and \
                "temp" not in params and \
                "stop_words" not in params:
            raise ValueError(f"params must contain top_p, top_k, max_tokens, temp or stop_tokens")
        if "top_p" in params:
            top_p = params.get("top_p")
            self.top_p = top_p
        if "top_k" in params:
            top_k = params.get("top_k")
            self.top_k = top_k
        if "temp" in params:
            temp = params.get("temp")
            self.temp = temp
        if "max_tokens" in params:
            max_tokens = params.get("max_tokens")
            self.max_tokens = max_tokens
        if "stop_words" in params:
            stop_tokens = params.get("stop_words")
            self._s = stop_tokens

    @params.deleter
    def params(self):
        """
        resets all params to default values
        :return:
        """
        self._p = self._default_p
        self._k = self._default_k
        self._t = self._default_t
        self._n = self._default_n
        self._s = self._default_stop

    @property
    def top_p(self) -> float:
        """
        returns the top_p parameter
        :return: a float representing the top_p parameter
        """
        return self._p

    @top_p.setter
    def top_p(self, top_p: float):
        """
        sets the top_p parameter
        :param top_p:
        :return:
        """
        if not isinstance(top_p, float) or isinstance(top_p, int):
            raise ValueError(f"top_p value must be a float, but got {type(top_p)}")
        if not (0 <= top_p <= 1):
            raise ValueError(f"top_p value must be between 0 and 1 inclusive, but got {top_p}")
        self._p = top_p

    @top_p.deleter
    def top_p(self):
        """
        resets the top_p parameter
        :return:
        """
        self._p = self._default_p

    @property
    def top_k(self) -> int:
        """
        returns the top_k parameter
        :return: a int representing the top_k parameter
        """
        return self._k

    @top_k.setter
    def top_k(self, k: int):
        """
        sets the top_k parameter
        :param k:
        :return:
        """
        if not isinstance(k, int):
            raise ValueError(f"top_k value must be an int, but got {type(k)}")
        if k < 1:
            raise ValueError(f"top_k value must be positive, but got {top_k}")
        self._k = k

    @top_k.deleter
    def top_k(self):
        """
        resets the top_k parameter
        :return:
        """
        self._k = self._default_k

    @property
    def temp(self) -> float:
        """
        returns the temp parameter
        :return: a float representing the temperature
        """
        return self._t

    @temp.setter
    def temp(self, temp: float):
        """
        sets the temp parameter
        :param temp:
        :return:
        """
        if not isinstance(temp, float) or isinstance(temp, int):
            raise ValueError(f"temp value must be float but got {type(temp)}")
        if not (0 <= temp <= 1) or not isinstance(temp, float):
            raise ValueError(f"temp value must be between 0 and 1, but got {temp}")
        self._t = temp

    @temp.deleter
    def temp(self):
        """
        resets the temp parameter
        :return:
        """
        self._t = self._default_t

    @property
    def max_tokens(self)->int:
        """
        returns the max_tokens parameter
        :return: the int max_tokens parameter
        """
        return self._n

    @max_tokens.setter
    def max_tokens(self, n_tokens: int):
        """
        sets the max_tokens parameter
        :param n_tokens:
        :return:
        """
        if not isinstance(n_tokens, int):
            raise ValueError(f"max_tokens value must be an int, but got {type(n_tokens)}")
        if n_tokens < 0 or not isinstance(n_tokens, int):
            raise ValueError(f"max_tokens value must be positive and an integer, but got {max_tokens}")
        self._n = n_tokens

    @max_tokens.deleter
    def max_tokens(self):
        """
        resets the max_tokens parameter
        :return:
        """
        self._n = self._default_n

    @property
    def stop_words(self) -> list:
        """
        returns the stop_words parameter
        :return: a list of stop words
        """

        return self._s

    @stop_words.setter
    def stop_words(self, stop_words: List[str]):
        """
        sets the stop_words parameter
        :param n_tokens:
        :return:
        """
        if not isinstance(stop_words, list):
            raise ValueError(f"stop_tokens must be a list, not a {type(stop_words)}")
        for i, item in enumerate(stop_words):
            if not isinstance(item, str):
                raise ValueError(f"stop_tokens must be a list of strings, but element {i} is a {type(item)}")
        self._s = stop_words

    @stop_words.deleter
    def stop_words(self):
        """
        resets the stop_words parameter
        :return:
        """
        self._s = self._default_stop

