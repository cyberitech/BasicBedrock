import abc
import json
import typing
from pydantic import BaseModel

class BaseAbstractRequest(BaseModel, extra='forbid'):

    @abc.abstractmethod
    def update_prompt(self,text):
        """
        Updates the prompt while maintaining its expected internal prompt structure
        Example, if the prompt must begin with 'Human:' this will be maintained
        :param text: the prompt you want to use
        :return:
        """
        raise NotImplementedError("Abstract method update_prompt not implemented")

    @abc.abstractmethod
    def update_prompt_raw(self,text):
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

    def get_json(self,indent:int=None):
        if not indent:
            return self.json()
        else:
            return json.dumps(
                json.loads(self.json()), indent=indent
            )

class BaseAbstractResponse(BaseModel):
    result_raw: dict = None

    def __init__(self, res:dict):
        super().__init__()
        self.result_raw = res

    @abc.abstractmethod
    def get_answer(self):
        """
        Returns only the answer to the prompt.  May be a string or a list in the case of embeddings.
        """
        raise NotImplementedError("Abstract method update_prompt_raw not implemented")

    def get_answer_raw(self)->dict:
        """
        Returns a copy of the dict object returned by the boto sdk
        """
        return self.result_raw.copy()

    def get_answer_json(self)->str:
        """
        returns the internal dict answer as a json string
        :return: json string
        """
        return json.dumps(self.result_raw)