"""
File containing all of the definitions and implementations for the Amazon family of requests and responses.
"""
from typing import List, Optional

from pydantic import BaseModel

from .baseclasses import BaseAbstractRequest, BaseAbstractResponse

AMAZON_TITAN_G1_LITE_CONTEXT_WINDOW = 4_000
AMAZON_TITAN_G1_EXPRESS_CONTEXT_WINDOW = 8_000
AMAZON_TITAN_TEXT_MAX_OUTPUT = 8_000

class AmazonTitanTextGenerationConfig(BaseModel):
    """
    Stub class for the configuration blob included as part of requests to Amazon Titan family models.
    the available hyperparameters are kept internally here and include P, temperate and max_tokens
    this model does not support K values.
    """
    maxTokenCount: int = 250
    stopSequences: List[Optional[str]] = []
    temperature: float = 0.5
    topP: float = 0.5


class AmazonTitanTextV1Request(BaseAbstractRequest):
    """
    All current Amazon Titan family models use the same request schema.
    This base class is used by both Amazon Titan Text G1 Express and Titan Text v1 Lite
    This model does not support top_k parameter.
    """
    inputText: str = "{PROMPT}"
    textGenerationConfig: AmazonTitanTextGenerationConfig = AmazonTitanTextGenerationConfig()

    def set_prompt(self, text):
        pass

    def set_prompt_raw(self, input_text):
        pass

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
        self.textGenerationConfig.maxTokenCount = min(max_tokens,AMAZON_TITAN_TEXT_MAX_OUTPUT)

    def set_p(self, top_p: float):
        """
        Sets top p of Amazon Titan model family
        :param top_p: float
        :return:
        """
        self.textGenerationConfig.topP = top_p

    def set_stop_words(self, stop_words: List[str]):
        """
        https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-text.html#model-parameters-titan-request-response
        Only valid stop words are "|", "User:" or none at all
        If no valid stop words are passed, the default of [] is used
        If a valid stop word is present in the list, the first one will be used
        :param stop_words:
        :return:
        """
        if not stop_words:
            self.textGenerationConfig.stopSequences = []
        else:
            # titan only accepts a single stop word.  and, it only accepts '| and 'User:' as a valid stop word
            # I want to ensure that if a valid stop word is given, we use the first one.
            # if no valid stop words are given, we wont use any
            if '|' not in stop_words and 'User:' not in stop_words:
                self.textGenerationConfig.stopSequences = []
            for word in stop_words:
                if word in ('|', 'User:'):
                    self.textGenerationConfig.stopSequences = [word]


class AmazonTitanTextG1LiteRequest(AmazonTitanTextV1Request):

    def set_prompt(self, text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        input_text = input_text[:AMAZON_TITAN_G1_LITE_CONTEXT_WINDOW]
        self.set_prompt_raw(input_text)

    def set_prompt_raw(self, text):
        self.inputText = text

    def get_prompt(self) -> str:
        return self.inputText


class AmazonTitanTextG1ExpressRequest(AmazonTitanTextV1Request):

    def set_prompt(self, text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        input_text = input_text[:AMAZON_TITAN_G1_EXPRESS_CONTEXT_WINDOW]
        self.set_prompt_raw(input_text)

    def set_prompt_raw(self, text):
        self.inputText = text

    def get_prompt(self) -> str:
        return self.inputText


class AmazonTitanTextV1Response(BaseAbstractResponse):
    """
    Response structure for Amazon Titan Text V1 API both Express and Lite
    """

    def get_answer(self) -> List[float]:
        return self.result_raw['results'][0]['outputText']


class AmazonTitanEmbedTextV1Request(BaseAbstractRequest):
    """
    Request structure for Amazon Titan Embedding V1 API
    This model accepts text and returns a list of floats, representing Amazon Titan embedding vectors.
    """
    inputText: str = "{PROMPT}"

    def get_prompt(self) -> str:
        return self.inputText

    def set_prompt(self, text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        self.set_prompt_raw(input_text)

    def set_prompt_raw(self, text):
        self.inputText = text

    def set_stop_words(self, stop_words: List[str]):
        pass

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
