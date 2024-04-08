"""
File containing all of the definitions and implementations for the Mistral family of requests and responses.
"""
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

    def update_prompt(self, text):
        input_text = "<s>[INST] {PROMPT} [/INST]"
        input_text = input_text.format(PROMPT=text)
        self.update_prompt_raw(input_text)

    def update_prompt_raw(self, text):
        self.prompt = text

    def set_p(self, top_p: float):
        self.top_p = top_p

    def set_k(self, top_k: int):
        self.top_k = top_k

    def set_temp(self, temp: float):
        self.temperature = temp

    def set_max_tokens(self, max_tokens: int):
        self.max_tokens = max_tokens


class MistralMistral7bInstructV0_2Request(MistralBaseRequest):
    """
    Request format for Mistral 7b Instruct V0:2
    This model supports temperature, top_p, top_k and max_tokens
    This class is implemented in MistralBaseRequest
    """


class MistralMistral8x7bInstructV0_1Request(MistralBaseRequest):
    """
    Request format for Mistral 8x7b Instruct V0:1
    This model supports temperature, top_p, top_k and max_tokens
    This class is implemented in MistralBaseRequest
    """


class MistralMistralLarge2402V1_0Request(MistralBaseRequest):
    """
    Request format for Mistral Large 2402 V1:0
    This model supports temperature, top_p, top_k and max_tokens
    This class is implemented in MistralBaseRequest
    """


class MistralBaseResponse(BaseAbstractResponse):
    """
    Base response format for Mistral Instruct family of models.
    """

    def get_answer(self) -> str:
        return self.result_raw['outputs'][0]['text']


class MistralMistral7bInstructV0_2Response(MistralBaseResponse):
    """
    Response format for Mistral 7b Instruct V0:2
    This class is implemented in MistralBaseResponse
    """


class MistralMistral8x7bInstructV0_1Response(MistralBaseResponse):
    """
    Response format for Mistral 8x7b Instruct V0:2
    This class is implemented in MistralBaseResponse
    """


class MistralMistralLarge2402V1_0Response(MistralBaseResponse):
    """
    Response format for Mistral Large 2402 v1:0
    This class is implemented in MistralInstructBaseResponse
    """
