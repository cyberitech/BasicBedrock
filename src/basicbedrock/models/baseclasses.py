import abc
import json
import typing
from pydantic import BaseModel


class Hyperparams(BaseModel, extra="forbid"):
    top_p: float = None
    top_k: int = None
    temp: float = None
    max_tokens: int = None


class BaseAbstractRequest(BaseModel, extra='forbid'):

    @abc.abstractmethod
    def update_prompt(self, text):
        """
        Updates the prompt while maintaining its expected internal prompt structure
        Example, if the prompt must begin with 'Human:' this will be maintained
        :param text: the prompt you want to use
        :return:
        """
        raise NotImplementedError("Abstract method update_prompt not implemented")

    @abc.abstractmethod
    def update_prompt_raw(self, text):
        """
        Updates the prompt without regards to any expected prompt structure.
        this is used for very precisely modifying prompts.
        :param text: the exact prompt you want to use
        :return:
        """
        raise NotImplementedError("Abstract method update_prompt_raw not implemented")

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
