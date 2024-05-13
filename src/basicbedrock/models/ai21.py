"""
File containing all of the definitions and implementations for the AI21 (jurassic) family of requests and responses.
"""
from typing import List, Optional

from pydantic import BaseModel

from .baseclasses import BaseAbstractRequest, BaseAbstractResponse

AI21_JURASSIC2_CONTEXT_WINDOW = 8_000
AI21_JURASSIC2_MAX_OUTPUT = 8_191


class AI21Jurassic2BaseRequest(BaseAbstractRequest):
    """
    AI21 Jurassic 2 request format.
    This model supports max_token, temperature and top_p, stop_sequences, count_penalty, presence_penalty and frequncy_penalty
    it does not support top_k
    as of right now there is no BasicBedrock support for penalty parameters
    """

    prompt: str = "{PROMPT}"
    maxTokens: int = 250
    temperature: float = 0.5
    topP: float = 0.5
    stopSequences: List = []

    def get_prompt(self) -> str:
        return self.prompt

    def set_prompt(self, text):
        """
        Update the prompt based on the input text.
        inserts text according to expected request conventions.
        :param text:
        :return:
        """
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        input_text = input_text[:AI21_JURASSIC2_CONTEXT_WINDOW]
        self.set_prompt_raw(input_text)

    def set_prompt_raw(self, text):
        """
        Update the prompt based on the input text without regards to expected input format
        what you insert, is inserted raw without formatting
        :param text:
        :return:
        """
        self.prompt = text

    def set_stop_words(self, stop_words: List[str]):
        """
        AI21 Jurassic 2 stop words allow either an empty list, or a single item of any string
        If more than a single stop word is provided, only the first element in the list will be used
        :param stop_words: a list of any stop words
        :return:
        """
        if not stop_words:
            self.stopSequences = []
        else:
            self.stopSequences = [stop_words[0]]

    def set_p(self, top_p: float):
        """
        Set the top_p parameter.
        :param top_p:
        :return:
        """
        self.topP = top_p

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
        self.maxTokens = min(max_tokens, AI21_JURASSIC2_MAX_OUTPUT)


class AI21Jurassic2BaseResponse(BaseAbstractResponse):
    """
    All AI21 Jurassic 2 models use the same response format.
    """

    def get_answer(self) -> List[float]:
        return self.result_raw['completions'][0]['data']['text']

