"""
File containing all of the definitions and implementations for the Meta family of requests and responses.
Amazon docs currently do not have request schemas for Llama 2 13b and Llama 2 70b, only the chat versions
"""
import typing

from baseclasses import BaseAbstractRequest, BaseAbstractResponse


class MetaLlama2ChatV1BaseRequest(BaseAbstractRequest):
    """
    Meta LLama 2 13b chat request format.
    This model supports max_token, temperature and top_p.
    It does not support top_k
    """
    prompt: str = "{PROMPT}"
    max_gen_len: int = 250
    temperature: float = 0.5
    top_p: float = 0.5

    def set_prompt(self, text):
        """
        Update the prompt based on the input text.
        inserts text according to expected request conventions.
        :param text:
        :return:
        """
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        self.set_prompt_raw(input_text)

    def set_prompt_raw(self, text):
        """
        Update the prompt based on the input text without regards to expected input format
        what you insert, is inserted raw without formatting
        :param text:
        :return:
        """
        self.prompt = text

    def set_stop_words(self, stop_words: typing.List[str]):
        """
        Meta Llama 2 models dont support stop words
        :param stop_words:
        :return:
        """
        pass


    def set_p(self, top_p: float):
        """
        Set the top_p parameter.
        :param top_p:
        :return:
        """
        self.top_p = top_p

    def set_k(self, top_k: int):
        """
        This model does not support top_k
        :param top_k:
        :return:
        """
        pass

    def set_temp(self, temp: float):
        """
        set the temperature parameter.
        :param temp:
        :return:
        """
        self.temperature = temp

    def set_max_tokens(self, max_tokens: int):
        """
        set the maximum tokens parameter.
        :param max_tokens:
        :return:
        """
        self.max_gen_len = max_tokens


class MetaLlama2ChatV1BaseResponse(BaseAbstractResponse):
    """
    Response format of Meta Llama 2 V1 family chat response.
    """

    def get_answer(self) -> str:
        return self.result_raw['generation']


