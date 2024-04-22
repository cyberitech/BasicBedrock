"""
File containing all of the definitions and implementations for the Mistral family of requests and responses.
"""
import typing

from .baseclasses import BaseAbstractRequest, BaseAbstractResponse


class MistralBaseRequest(BaseAbstractRequest):
    """
    Base request for Mistral family of models.
    this mnodel supports temperature, top_p, top_k and max_tokens
    """
    prompt: str = "<s>[INST] this is where you place your input text [/INST]"
    max_tokens: int = 250
    temperature: float = 0.5
    top_p: float = 0.5
    top_k: int = 125
    stop: typing.List[str] = []

    def set_prompt(self, text):
        input_text = "<s>[INST] {PROMPT} [/INST]"
        input_text = input_text.format(PROMPT=text)
        self.set_prompt_raw(input_text)

    def set_prompt_raw(self, text):
        self.prompt = text

    def set_stop_words(self, stop_words: typing.List[str]):
        """
        Mistral models seem to accept any number of stop words in any format
        :param stop_words:
        :return:
        """
        self.stop = stop_words

    def set_p(self, top_p: float):
        self.top_p = top_p

    def set_k(self, top_k: int):
        self.top_k = top_k

    def set_temp(self, temp: float):
        self.temperature = temp

    def set_max_tokens(self, max_tokens: int):
        self.max_tokens = max_tokens


class MistralBaseResponse(BaseAbstractResponse):
    """
    Base response format for Mistral Instruct family of models.
    """

    def get_answer(self) -> str:
        return self.result_raw['outputs'][0]['text']
