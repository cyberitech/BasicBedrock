"""
File containing all of the definitions and implementations for the Cohere family of requests and responses.
"""
import typing
from typing import List

from baseclasses import BaseAbstractRequest, BaseAbstractResponse

COHERE_COMMAND_TEXT_CONTEXT_WINDOW = 4_000
COHERE_COMMAND_R_RPLUS_CONTEXT_WINDOW = 128_000 - 1
COHERE_COMMAND_TEXT_MAX_OUTPUT = 4_096
COHERE_COMMAND_R_MAX_OUTPUT = 127_894 # undocumented.  Trial and error
COHERE_COMMAND_RPLUS_MAX_OUTPUT = 115_000 # somewhere between 115_000 and 120_00. didnt want to test



class CohereCommandTextBaseRequest(BaseAbstractRequest):
    """
    This is the base request format that all Cohere text-family models use
    These models support top_p, top_k, max_tokens and temperature.
    """
    prompt: str = "{PROMPT}"
    max_tokens: int = 250
    temperature: float = 0.5
    p: float = 0.5
    k: int = 125
    stop_sequences: List[str] = []

    def get_prompt(self) -> str:
        return self.prompt

    def set_prompt(self, text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        input_text = input_text[:COHERE_COMMAND_TEXT_CONTEXT_WINDOW]
        self.set_prompt_raw(input_text)

    def set_prompt_raw(self, text):
        self.prompt = text

    def set_stop_words(self, stop_words: typing.List[str]):
        """
        Cohere seems to accept any number of stop words
        :param stop_words:
        :return:
        """
        self.stop_sequences = stop_words

    def set_p(self, top_p: float):
        self.p = top_p

    def set_k(self, top_k: int):
        self.k = top_k

    def set_temp(self, temp: float):
        self.temperature = temp

    def set_max_tokens(self, max_tokens: int):
        self.max_tokens = min(max_tokens, COHERE_COMMAND_TEXT_MAX_OUTPUT)


class CohereCommandTextBaseResponse(BaseAbstractResponse):
    """
    this is the base response format used by all text-family cohere models
    """

    def get_answer(self) -> str:
        return self.result_raw['generations'][0]['text']


"""
Cohere Embed English V3
"""


class CohereEmbedBaseRequest(BaseAbstractRequest):
    """
    All cohere command models use the same request format.
    Models support input text only.
    """
    texts: List[str] = ["{PROMPT}"]
    input_type: str = "search_document"

    def get_prompt(self) -> str:
        return self.texts[0]

    def set_prompt(self, text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        texts = [input_text]
        self.set_prompt_raw(texts)

    def set_prompt_raw(self, texts: list):
        self.texts = texts

    def set_stop_words(self, stop_words: typing.List[str]):
        pass

    def set_p(self, top_p: float):
        """
        Cohere Embed V3 does not support top_p
        :param top_p:
        :return:
        """
        pass

    def set_k(self, top_k: int):
        """
        Cohere Embed V3 does not support top_k
        :param top_k:
        :return:
        """
        pass

    def set_temp(self, temp: float):
        """
        Cohere Embed V3 does not support temperature
        :param temp:
        :return:
        """
        pass

    def set_max_tokens(self, max_tokens: int):
        """
        Cohere Embed V3 does not support max_tokens
        :param max_tokens:
        :return:
        """
        pass


class CohereEmbedBaseResponse(BaseAbstractResponse):
    """
    All Cohere Embed models use the same response format.
    """

    def get_answer(self) -> List[float]:
        return self.result_raw['embeddings'][0]


class CohereCommandRPLUSTextBaseRequest(BaseAbstractRequest):

    message: str = "{PROMPT}"
    max_tokens: int = 250
    temperature: float = 0.5
    p: float = 0.5
    k: int = 125
    stop_sequences: List[str] = []

    def set_prompt(self, text: str):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        input_text = input_text[:COHERE_COMMAND_R_RPLUS_CONTEXT_WINDOW]
        self.set_prompt_raw(input_text)

    def set_prompt_raw(self, text: str):
        self.message = text

    def set_stop_words(self, stop_words: typing.List[str]):
        self.stop_sequences = stop_words

    def get_prompt(self) -> str:
        return self.message

    def set_p(self, top_p: float):
        self.p = top_p

    def set_k(self, top_k: int):
        self.k=top_k

    def set_temp(self, temp: float):
        self.temperature = temp

    def set_max_tokens(self, max_tokens: int):
        self.max_tokens = min(max_tokens, COHERE_COMMAND_TEXT_MAX_OUTPUT)


class CohereCommandRPLUSTextBaseResponse(BaseAbstractResponse):
    """
    this is the base response format used by all text-family cohere models
    """

    def get_answer(self) -> str:
        return self.result_raw['text']