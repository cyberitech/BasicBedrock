"""
File containing the base classes used for all model requests and responses.
Contains abstract base classes for the requests and responses, as well as a concrete class for hyperparameters p, k, temp and max_tokens
"""
import abc
import json
import typing

from pydantic import BaseModel


class Hyperparams(BaseModel, extra="forbid"):
    """
    Hyperparameters for a model.
    Values are top_p, top_k, temp and max_tokens
    Not all models support all parameters.
    Any parameters used in here which are not supported by the model are ignored at runtime
    """
    top_p: float = None
    top_k: int = None
    temp: float = None
    max_tokens: int = None
    stop_words: typing.List[str] = []


class BaseAbstractRequest(BaseModel, extra='forbid'):
    """
    Abstract base class for all model requests. All model requests must inherit this class.\n
    update_prompt and update_promp_raw differ in the fact that some models expect a certain request format to work properly,
    eg, in certain cases boto3 may reject the request if the prompt does not begin with "Human:"\
    update_prompt will format all prompts as expected by the model, whereas update_prompt_raw will input text without formatting.
    The other abstract methods all deal with setting hyperparam values P, K, temp, and max tokens.\n
    Additionally, two non abstract methods allow the caller to return the request as a dict or json.\n
    """

    @abc.abstractmethod
    def set_prompt(self, text: str):
        """
        Updates the prompt while maintaining its expected internal prompt structure\n
        Example, if the prompt must begin with 'Human:' this will be maintained\n
        :param text: the prompt you want to use
        :return:
        """
        raise NotImplementedError("Abstract method update_prompt not implemented")

    @abc.abstractmethod
    def set_prompt_raw(self, text: str):
        """
        Updates the prompt without regards to any expected prompt structure.\n
        this is used for very precisely modifying prompts.\n
        :param text: the exact prompt you want to use
        :return:
        """
        raise NotImplementedError("Abstract method update_prompt_raw not implemented")

    @abc.abstractmethod
    def set_stop_words(self, stop_words: typing.List[str]):
        """
        Sets the stop words used in the model.\n
        If the model does not support stop words, this is ignored\n
        :param stop_words: the list of strings
        :return:
        """

    @abc.abstractmethod
    def get_prompt(self) -> str:
        """
        This retrieves only the current prompt from the model request structure.
        :return: a str containing the extracted prompt
        """

    def get_dict(self):
        j = json.loads(self.json())
        return j

    def get_json(self, indent: int = None):
        if not indent:
            return self.json()
        else:
            return json.dumps(
                json.loads(self.json()), indent=indent
            )

    def set_params(self, params: dict):
        """
        Sets the hyperparameters of the request (p, k, temp, max_tokens)
        :param params:
        :return:
        """
        if not isinstance(params, dict):
            raise TypeError(f"params must be a dict, got {type(params)}")
        hparams = Hyperparams(**params)
        if hparams.temp is not None:
            self.set_temp(hparams.temp)
        if hparams.top_k is not None:
            self.set_k(hparams.top_k)
        if hparams.top_p is not None:
            self.set_p(hparams.top_p)
        if hparams.max_tokens is not None:
            self.set_max_tokens(hparams.max_tokens)
        if hparams.stop_words is not None:
            self.set_stop_words(hparams.stop_words)

    @abc.abstractmethod
    def set_p(self, top_p: float):
        raise NotImplementedError("Abstract method set_p not implemented")

    @abc.abstractmethod
    def set_k(self, top_k: int):
        raise NotImplementedError("Abstract method set_k not implemented")

    @abc.abstractmethod
    def set_temp(self, temp: float):
        raise NotImplementedError("Abstract method set_temp not implemented")

    @abc.abstractmethod
    def set_max_tokens(self, max_tokens: int):
        raise NotImplementedError("Abstract method set_max_tokens not implemented")


class BaseAbstractResponse(BaseModel):
    """
    This is the abstract base model for all model responses.
    It will internally store the exact result provided by boto3 as a dict.
    methods are exposed to return to the caller the raw response as dict or json.
    The abstract method get_answer serves to parse out the actual response and return it, ignoring the associated metadata.
    """
    result_raw: dict = None

    def __init__(self, res: dict):
        super().__init__()
        self.result_raw = res

    @abc.abstractmethod
    def get_answer(self):
        """
        Returns only the answer to the prompt.  May be a string or a list in the case of embeddings.
        """
        raise NotImplementedError("Abstract method update_prompt_raw not implemented")

    def get_answer_raw(self) -> dict:
        """
        Returns a copy of the dict object returned by the boto sdk
        """
        return self.result_raw.copy()

    def get_answer_json(self) -> str:
        """
        returns the internal dict answer as a json string
        :return: json string
        """
        return json.dumps(self.result_raw)
