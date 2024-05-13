"""
File containing all of the definitions and implementations for the Mistral family of requests and responses.
"""
import typing

from .baseclasses import BaseAbstractRequest, BaseAbstractResponse

MISTRAL_CONTEXT_WINDOW = 32_000 - 1
MISTRAL_7B_INSTRUCT_MAX_OUTPUT = 8_192
MISTRAL_8X7B_INSTRUCT_MAX_OUTPUT = 4_096
MISTRAL_LARGE_MAX_OUTPUT = 4_096  # docs claim its 8_192 but this is apparently not true, it fails boto3 validation


class MistralBaseRequest(BaseAbstractRequest):
    """
    Base request for Mistral family of models.
    this mnodel supports temperature, top_p, top_k and max_tokens
    """
    prompt: str = "<s>[INST] {PROMPT} [/INST]"
    max_tokens: int = 250
    temperature: float = 0.5
    top_p: float = 0.5
    top_k: int = 125
    stop: typing.List[str] = []

    def get_prompt(self) -> str:
        return self.prompt

    def set_prompt(self, text):
        prompt = "<s>[INST] {PROMPT} [/INST]"
        padding = len(prompt.replace("{PROMPT}",""))
        cut_text = text[:MISTRAL_CONTEXT_WINDOW-padding]
        prompt = prompt.format(PROMPT=cut_text)
        self.set_prompt_raw(prompt)

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

    def set_max_tokens(self, top_p: float):
        pass


class Mistral7BInstructRequest(MistralBaseRequest):

    def set_max_tokens(self, max_tokens: int):
        self.max_tokens = min(max_tokens, MISTRAL_7B_INSTRUCT_MAX_OUTPUT)


class Mistral8X7BInstructRequest(MistralBaseRequest):

    def set_max_tokens(self, max_tokens: int):
        self.max_tokens = min(max_tokens, MISTRAL_8X7B_INSTRUCT_MAX_OUTPUT)


class MistralLargeRequest(MistralBaseRequest):

    def set_max_tokens(self, max_tokens: int):
        self.max_tokens = min(max_tokens, MISTRAL_LARGE_MAX_OUTPUT)


class MistralBaseResponse(BaseAbstractResponse):
    """
    Base response format for Mistral Instruct family of models.
    """

    def get_answer(self) -> str:
        return self.result_raw['outputs'][0]['text']
