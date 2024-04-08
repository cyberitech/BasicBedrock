"""
Basic Bedrock Python API abstraction.
Currently supports all text-modal foundation models in AWS Bedrock.
Abstracts away the need to understand any of the model-specific response or request semantics.
Simply pick a model, and invoke it with a prompt.
If you with to specify k, p, temp, and max_token parameters, they will be applied on a best effort basis.
not all models support all parameters.
"""

import json
import typing
import warnings

import boto3
import pydantic

from models import *


class BasicBedrock(object):
    def __init__(self, session: boto3.session.Session = None, **kwargs):
        """
        Creates an instance of basic bedrock.
        session param is optional.  If omitted, a default session will be used.
        Right now, the only kwargs supported are a param dictionary.
        Param dicts are in the format of {'top_p': float, 'top_k': int, 'temp': float, 'max_tokens': int}
        :param session: the boto3 session to use for creating the basic bedrock instance
        :param kwargs: kwargs used are in the format of {'top_p': float, 'top_k': int, 'temp': float, 'max_tokens': int}
        """
        if not session:
            warnings.warn('No session provided, attemtping to use "default" profile', category=RuntimeWarning)
            session = boto3.session.Session(profile_name='default')
        self.client = session.client("bedrock-runtime")
        self._default_k = 100
        self._default_p = .5
        self._default_t = .5
        self._default_n = 150
        self._k = kwargs.get('top_k', self._default_k)
        self._p = kwargs.get('top_p', self._default_p)
        self._t = kwargs.get('temp', self._default_t)
        self._n = kwargs.get('max_tokens', self._default_n)

    def print_available_models(self) -> None:
        """
        Prints all available models line by line
        :return: None
        """
        print(os.linesep.join(self.get_available_models()))

    def get_available_models(self) -> list:
        """
        returns a list of all available models
        :return: ["model1", "model2", "model3"...]
        """
        return sorted(model_request_mapping.keys())

    def get_model_schema_dict(self, model_id: str) -> dict:
        """
        returns a dict object representing the request scheme of model_id
        :param model_id:  the chosen model id
        :return: dict object representing the base request scheme of model_id
        """
        if model_id not in self.get_available_models():
            raise ValueError(f"requested model {model_id} is not an available model")
        else:
            model = model_request_mapping.get(model_id)
            _inst = model()
            j = _inst.json()
            d = json.loads(j)
            return d

    def get_model_request_object(self, model_id: str) -> BaseAbstractRequest:
        """
        returns an instantiated object representing the schema for the chosen model.
        All these inherit from BaseSchemaAbstract.
        Its useful for when you want to use BaseSchemaAbstract to modify prompts and produce json or dicts manually
        :param model_id: the chosen model ID
        :return: the schema class object for the chosen model, it will be a subclass of a BaseAbstractRequest
        """
        if model_id not in self.get_available_models():
            raise ValueError(f"requested model {model_id} is not an available model")
        _inst = model_request_mapping.get(model_id)()
        return _inst

    def get_model_request_json(self, model_id: str) -> str:
        """
        returns a string object representing the request scheme of model_id in json format
        :param model_id:  the chosen model id
        :return: a json string
        """
        if model_id not in self.get_available_models():
            raise ValueError(f"requested model {model_id} is not an available model")
        else:
            model = model_request_mapping.get(model_id)
            _inst = model()
            j = _inst.json()
            return j

    def print_model_schema(self, model_id: str, indent: int = None) -> None:
        """
        prints the request scheme of model_id in a pretty format.
        if indent is not None, indent the lines when printing
        :param model_id: the chosen model id
        :param indent: how many spaces to indent, default=4
        :return: None
        """
        if model_id not in self.get_available_models():
            raise ValueError(f"requested model {model_id} is not an available model")
        else:
            model = model_request_mapping.get(model_id)
            _inst = model()
            j = _inst.json()
            if indent:
                j = json.dumps(json.loads(j), indent=indent)
        print(j)

    def invoke(self, model_id: str, request: typing.Union[str, dict],
               show_request: bool = False) -> BaseAbstractResponse:
        """
        invokes a model_id and returns the response.  Non-streaming only.
        request may by one of: a prompt, a json string represent the request schema, or a dict representing the request schema
        invoking with a request of a string containing valid json data, if it is not a valid json schema for the model
        it will be interpreted as a prompt string and a runtime warning will be raised
        :param model_id: the model id you wish to invoke
        :param request: a string or dict representing either a prompt or a model request schema
        :param show_request: prints the request blob before invoking
        :return: the response to the request, as a subclass of a model.BaseAbstractResponse
        """

        if not isinstance(request, dict) and not isinstance(request, str):
            raise TypeError(f"request must be a string, or a json dict representing the request schema for the model, "
                            f"found: {type(request)}")
        schema_obj: BaseAbstractRequest = model_request_mapping.get(model_id)
        if schema_obj is None:
            raise ValueError(f"requested model {model_id} is not an available model")
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
            schema_inst.update_prompt(request)
        schema_inst.set_params(self.params)
        body = schema_inst.json()
        full_request = {
            "modelId": model_id,
            "body": body
        }
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
            "max_tokens": self._n
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
                "temp" not in params:
            raise ValueError(f"params must contain top_p, top_k, max_tokens or temp")
        if "top_p" in params:
            self.top_p = params["top_p"]
        if "top_k" in params:
            self.top_k = params["top_k"]
        if "temp" in params:
            self.temp = params["temp"]
        if "max_tokens" in params:
            self.max_tokens = params["max_tokens"]

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

    @property
    def top_p(self) -> float:
        """
        returns the top_p parameter
        :return:
        """
        return self._p

    @top_p.setter
    def top_p(self, top_p: float):
        """
        sets the top_p parameter
        :param top_p:
        :return:
        """
        if not (0 < top_p <= 1) or not isinstance(top_p, float):
            raise ValueError(f"top_p value must be between 0 and 1, but got {top_p}")
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
        :return:
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
        if k < 1 or not isinstance(k, int):
            raise ValueError(f"top_k value must be positive and an integer, but got {top_k}")
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
        :return:
        """
        return self._t

    @temp.setter
    def temp(self, temp: float):
        """
        sets the temp parameter
        :param temp:
        :return:
        """
        if not isinstance(temp, float):
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
    def max_tokens(self):
        """
        returns the max_tokens parameter
        :return:
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
