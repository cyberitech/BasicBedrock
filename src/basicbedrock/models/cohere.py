"""
File containing all of the definitions and implementations for the Cohere family of requests and responses.
"""
from typing import List

from baseclasses import BaseAbstractRequest, BaseAbstractResponse


class CohereCommandBaseRequest(BaseAbstractRequest):
    """
    This is the base request format that all Cohere text-family models use
    These models support top_p, top_k, max_tokens and temperature.
    """
    prompt: str = "{PROMPT}"
    max_tokens: int = 250
    temperature: float = 0.5
    p: float = 0.5
    k: int = 125

    def update_prompt(self, text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        self.update_prompt_raw(input_text)

    def update_prompt_raw(self, text):
        self.prompt = text

    def set_p(self, top_p: float):
        self.p = top_p

    def set_k(self, top_k: int):
        self.k = top_k

    def set_temp(self, temp: float):
        self.temperature = temp

    def set_max_tokens(self, max_tokens: int):
        self.max_tokens = max_tokens


class CohereCommandTextV14Request(CohereCommandBaseRequest):
    """
    Cohere Command Text V14 supports top_p, top_k, temperature and max_tokens
    all functionality is implemented in CohereCommandBaseRequest
    """


class CohereCommandLightTextV14Request(CohereCommandBaseRequest):
    """
    Cohere Command Light Text V14 supports top_p, top_k, temperature and max_tokens
    all functionality is implemented in CohereCommandBaseRequest
    """


class CohereCommandTextBaseResponse(BaseAbstractResponse):
    """
    this is the base response format used by all text-family cohere models
    """

    def get_answer(self) -> str:
        return self.result_raw['generations'][0]['text']


class CohereCommandTextV14Response(CohereCommandTextBaseResponse):
    """
    This is the response format for Cohere Command Text v14
    It is implemented in CohereCommandTextBaseResponse
    """


class CohereCommandLightTextV14Response(CohereCommandTextBaseResponse):
    """
    This is the response format for Cohere Command Light Text v14
    It is implemented in CohereCommandTextBaseResponse
    """


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

    def update_prompt(self, text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        texts = [input_text]
        self.update_prompt_raw(texts)

    def update_prompt_raw(self, texts: list):
        self.texts = texts

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


class CohereEmbedEnglishV3Request(CohereEmbedBaseRequest):
    """
    Request for Cohere Embed English V3.
    It supports top_p, top_k, temperature and max_tokens
    it is implemented in CohereEmbedBaseRequest
    """


class CohereEmbedMultilingualV3Request(CohereEmbedBaseRequest):
    """
    Request for Cohere Embed Multilingual V3.
    It supports top_p, top_k, temperature and max_tokens
    it is implemented in CohereEmbedBaseRequest
    """


class CohereEmbedBaseResponse(BaseAbstractResponse):
    """
    All Cohere Embed models use the same response format.
    """

    def get_answer(self) -> List[float]:
        return self.result_raw['embeddings'][0]


class CohereEmbedEnglishV3Response(CohereEmbedBaseResponse):
    """
    Response format for Cohere Embed English V3
    It is implemented in CohereEmbedBaseResponse
    """


class CohereEmbedMultilingualV3Response(CohereEmbedBaseResponse):
    """
    Response for Cohere Embed Multilingual V3.
    it is implemented in CohereEmbedBaseResponse
    """
