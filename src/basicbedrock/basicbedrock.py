import json
import boto3
import warnings
import typing
import pydantic
from models import *

class BasicBedrock(object):
    def __init__(self, session:boto3.session.Session=None):
        if not session:
            warnings.warn('No session provided, attemtping to use "default" profile',category=RuntimeWarning)
            session = boto3.session.Session(profile_name='default')
        self.client = session.client("bedrock-runtime")


    def print_available_models(self)->None:
        """
        Prints all available models
        :return: None
        """
        print(os.linesep.join(self.get_available_models()))

    def get_available_models(self)->list:
        """
        returns a list of all available models
        :return: ["model1", "model2", "model3"...]
        """
        return sorted(model_request_mapping.keys())

    def get_model_schema_dict(self, model_id:str)->dict:
        """
        returns a dict object representing the request scheme of model_id
        :param model_id:  the chosen model id
        :return:
        """
        if model_id not in self.get_available_models():
            raise ValueError(f"requested model {model_id} is not an available model")
        else:
            model = model_request_mapping.get(model_id)
            _inst = model()
            j = _inst.json()
            d = json.loads(j)
            return d

    def get_model_schema_object(self, model_id:str)->BaseAbstractRequest:
        """
        returns an instantiated object representing the schema for the chosen model.
        All these inherit from BaseSchemaAbstract.
        Its useful for when you want to use BaseSchemaAbstract to modify prompts and produce json or dicts manually
        :param model_id: the chosen model ID
        :return: the schema class object for the chosen model
        """
        if model_id not in self.get_available_models():
            raise ValueError(f"requested model {model_id} is not an available model")
        _inst = model_request_mapping.get(model_id)()
        return _inst

    def get_model_schema_json(self, model_id:str)->str:
        """
        returns a string object representing the request scheme of model_id in json format
        :param model_id:  the chosen model id
        :return:
        """
        if model_id not in self.get_available_models():
            raise ValueError(f"requested model {model_id} is not an available model")
        else:
            model = model_request_mapping.get(model_id)
            _inst = model()
            j = _inst.json()
            return j

    def print_model_schema(self,model_id:str,indent:int=None)->None:
        """
        prints the request scheme of model_id in a pretty format.
        if indent is not None, indent the lines when printing
        :param model_id: the chosen model id
        :param indent: how many spaces to indent, default=4
        :return:
        """
        if model_id not in self.get_available_models():
            raise ValueError(f"requested model {model_id} is not an available model")
        else:
            model = model_request_mapping.get(model_id)
            _inst = model()
            j = _inst.json()
            if indent:
                j = json.dumps(json.loads(j),indent=indent)
        print(j)

    def invoke(self,model_id:str,request:typing.Union[str,dict], show_request:bool = False)->BaseAbstractResponse:
        """
        invokes a model_id and returns the response.  Non-streaming only.
        request may by one of: a prompt, a json string represent the request schema, or a dict representing the request schema
        invoking with a request of a string containing valid json data, if it is not a valid json schema for the model
        it will be interpreted as a prompt string and a runtime warning will be raised
        :param request: a string or dict representing either a prompt or a model request schema
        :return: the response to the request
        """

        if not isinstance(request,dict) and not isinstance(request,str):
            raise TypeError(f"request must be a string, or a json dict representing the request schema for the model, "
                            f"found: {type(request)}")
        schema_obj:BaseAbstractRequest = model_request_mapping.get(model_id)
        if schema_obj is None:
            raise ValueError(f"requested model {model_id} is not an available model")
        schema_inst = None
        if isinstance(request,dict):
            # infer if the request is valid
            try:
                schema_inst = schema_obj.parse_obj(request)
            except pydantic.ValidationError:
                schema_inst = schema_obj()
                valid_j = schema_inst.json()
                invalid_j = json.dumps(request)
                raise ValueError(f"inavlid request dict was provided for {model_id}.. wanted: {valid_j} but received: {invalid_j}")
        elif isinstance(request,str):
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
            raise RuntimeError(f"Encountered a non-200 status code {r['ResponseMetadata']['HTTPStatusCode']}, Code: {code}, Message: {message}")
        resp_body = r.get('body')
        resp_body = resp_body.read()
        resp_body = json.loads(resp_body)

        response_obj = model_response_mapping.get(model_id)
        response_inst = response_obj(res=resp_body)
        return response_inst

