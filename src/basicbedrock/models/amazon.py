"""
File containing all of the definitions and implementations for the Amazon family of requests and responses.
"""
from typing import List, Optional

from pydantic import BaseModel

from .baseclasses import BaseAbstractRequest, BaseAbstractResponse


class AmazonTitanTextGenerationConfig(BaseModel):
    """
    Stub class for the configuration blob included as part of requests to Amazon Titan family models.
    the available hyperparameters are kept internally here and include P, temperate and max_tokens
    this model does not support K values.
    """
    maxTokenCount: int = 1000
    stopSequences: List[Optional[str]] = []
    temperature: float = 0.5
    topP: float = 1.


class AmazonTitanBaseModelRequest(BaseAbstractRequest):
    """
    All current Amazon Titan family models use the same request schema.
    This base class is used by both Amazon Titan Text G1 Express and Titan Text v1 Lite
    This model does not support top_k parameter.
    """
    inputText: str = "{PROMPT}"
    textGenerationConfig: AmazonTitanTextGenerationConfig = AmazonTitanTextGenerationConfig()

    def update_prompt(self, text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        self.update_prompt_raw(input_text)

    def update_prompt_raw(self, text):
        self.inputText = text

    def set_k(self, top_k: int):
        """
        Top K is not supported by Amazon Titan model family.  This method does nothing.
        :param top_k: int
        :return:
        """
        pass

    def set_temp(self, temp: float):
        """
        Sets temperature of Amazon Titan model family
        :param temp: flat
        :return:
        """
        self.textGenerationConfig.temperature = temp

    def set_max_tokens(self, max_tokens: int):
        """
        sets max token output of Amazon Titan model family
        :param max_tokens: int
        :return:
        """
        self.textGenerationConfig.maxTokenCount = max_tokens

    def set_p(self, top_p: float):
        """
        Sets top p of Amazon Titan model family
        :param top_p: float
        :return:
        """
        self.textGenerationConfig.topP = top_p


class AmazonTitanTextExpressV1Request(AmazonTitanBaseModelRequest):
    """
    Request structure for Amazon Titan Text Express V1 API.
    This model accepts text and returns text.
    This model does not support K parameter.

    Please see AmazonTitanBaseModelRequest for the implementation of all methods
    """


class AmazonTitanTextLiteV1Request(AmazonTitanBaseModelRequest):
    """
    Request structure for Amazon Titan Text Lite V1 API
    This model accepts text and returns text.
    This model does not support K parameter.

    Please see AmazonTitanBaseModelRequest for the implementation of all methods
    """


class AmazonTitanTextV1Response(BaseAbstractResponse):
    """
    Response structure for Amazon Titan Text V1 API both Express and Lite
    """

    def get_answer(self) -> List[float]:
        return self.result_raw['results'][0]['outputText']


class AmazonTitanTextExpressV1Response(AmazonTitanTextV1Response):
    """
    Response structure for Amazon Titan Text Express V1 API.
    Implemented in AmazonTitanTextV1Response
    """


class AmazonTitanTextLiteV1Response(AmazonTitanTextV1Response):
    """
    Response structure for Amazon Titan Text Lite V1 API.
    Implemented in AmazonTitanTextV1Response
    """


class AmazonTitanEmbedTextV1Request(BaseAbstractRequest):
    """
    Request structure for Amazon Titan Embedding V1 API
    This model accepts text and returns a list of floats, representing Amazon Titan embedding vectors.
    """
    inputText: str = "{PROMPT}"

    def update_prompt(self, text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        self.update_prompt_raw(input_text)

    def update_prompt_raw(self, text):
        self.inputText = text

    def set_k(self, top_k: int):
        """
        Top K is not supported by Amazon Titan Embedding V1 API
        :param top_k:
        :return:
        """
        pass

    def set_temp(self, temp: float):
        """
        Sets temperature of Amazon Titan Embedding V1 API
        :param temp:
        :return:
        """
        pass

    def set_max_tokens(self, max_tokens: int):
        """
        Sets max token output of Amazon Titan Embedding V1 API
        :param max_tokens:
        :return:
        """
        pass

    def set_p(self, top_p: float):
        """
        Sets top p of Amazon Titan Embedding V1 API
        :param top_p:
        :return:
        """
        pass


class AmazonTitanEmbedTextV1Response(BaseAbstractResponse):
    """
    Response structure for Amazon Titan Embedding V1 API both Express and Lite
    """

    def get_answer(self) -> List[float]:
        return self.result_raw['embedding']
