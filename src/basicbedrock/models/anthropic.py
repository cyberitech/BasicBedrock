"""
File containing all of the definitions and implementations for the Anthropic family of requests and responses.
"""
from typing import List

from pydantic import BaseModel

from baseclasses import BaseAbstractRequest, BaseAbstractResponse


class AnthropicV1V2BaseModelRequest(BaseAbstractRequest):
    """
    Claude V1 and V2 family models all utilize the same request/response format
    This handles all the logic for them
    this model supports temp, top_k, top_p, stop sequences and max_tokens
    """
    prompt: str = "\n\nHuman: {PROMPT}\n\nAssistant:"
    max_tokens_to_sample: int = 300
    temperature: float = 0.5
    top_k: int = 250
    top_p: float = 1.
    stop_sequences: list = ["\n\nHuman:"]
    anthropic_version: str = "bedrock-2023-05-31"

    def update_prompt(self, text):
        prompt = f"\n\nHuman: {text}\n\nAssistant:"
        self.update_prompt_raw(prompt)

    def update_prompt_raw(self, text):
        self.prompt = text

    def set_p(self, top_p: float):
        self.top_p = top_p

    def set_k(self, top_k: int):
        self.top_k = top_k

    def set_temp(self, temp: float):
        self.temperature = temp

    def set_max_tokens(self, max_tokens: int):
        self.max_tokens_to_sample = max_tokens


class AnthropicClaudeInstantV1Request(AnthropicV1V2BaseModelRequest):
    """
    Anthropic Claude Instant V1 model supports temp, top_k, top_p, stop_sequences and max_tokens
    All functionality is implemented in the superclass AnthropicV1V2BaseModelRequest
    """


class AnthropicClaudeV2Request(AnthropicV1V2BaseModelRequest):
    """
    Anthropic Claude V2 model supports temp, top_k, top_p, stop_sequences and max_tokens
    All functionality is implemented in the superclass AnthropicV1V2BaseModelRequest
    """


class AnthropicClaudeV2_1Request(AnthropicV1V2BaseModelRequest):
    """
    Anthropic Claude V2:1 model supports temp, top_k, top_p, stop_sequences and max_tokens
    All functionality is implemented in the superclass AnthropicV1V2BaseModelRequest
    """


class AnthropicClaudeV1V2BaseModelResponse(BaseAbstractResponse):
    """
    Claude V1 and V2 family models all utilize the same response/response format
    Every Calude V1 and V2 model response will inherit this class
    """

    def get_answer(self) -> List[float]:
        return self.result_raw['completion']


class AnthropicClaudeInstantV1Response(AnthropicClaudeV1V2BaseModelResponse):
    """
    The class representing the response of Anthropic Claude Instant V1 model
    this class is implemented in the superclass AnthropicV1V2BaseModelResponse
    """


class AnthropicClaudeV2Response(AnthropicClaudeV1V2BaseModelResponse):
    """
    The class representing the response of Anthropic Claude V2 model
    this class is implemented in the superclass AnthropicV1V2BaseModelResponse
    """


class AnthropicClaudeV2_1Response(AnthropicClaudeV1V2BaseModelResponse):
    """
    The class representing the response of Anthropic Claude V2:1 model
    this class is implemented in the superclass AnthropicV1V2BaseModelResponse
    """


class AntropicClaude3MessageContent(BaseModel):
    """
    Stub class for the Antropic Claude V3 message content field.
    it contains information about the content of the input (is it text or image) as well as the input itself
    """
    type: str = "text"
    text: str = '\n\nHuman: {PROMPT}\n\nAssistant:'

    def update_prompt(self, text):
        text = f'\n\nHuman: {text}\n\nAssistant:'
        self.update_prompt_raw(text)

    def update_prompt_raw(self, text):
        self.text = text


class AntropicClaude3Message(BaseModel):
    """
    Stub class for the Antropic Claude V3 message content field.
    this contains metadata about the request, such as the role, as well as a list of AntropicClaude3MessageContent classes
    """
    role: str = "user"
    content: List[AntropicClaude3MessageContent] = [AntropicClaude3MessageContent()]

    def update_prompt(self, text):
        self.content[0].update_prompt(text)

    def update_prompt_raw(self, text):
        self.content[0].update_prompt_raw(text)


class AnthropicClaude3SonnetHaikuBaseRequest(BaseAbstractRequest):
    """
    This class represents the request format used by Anthropic Claude V3 family of models
    Both Haiku and Sonnet use this request format.
    The model supports temp, top_k, top_p, stop_sequences and max_tokens
    """
    max_tokens: int = 300
    top_p: float = 1.
    top_k: int = 25
    temperature: float = 0.5
    messages: List[AntropicClaude3Message] = [AntropicClaude3Message()]
    anthropic_version: str = "bedrock-2023-05-31"

    def update_prompt(self, text):
        self.messages[0].update_prompt(text)

    def update_prompt_raw(self, text):
        self.messages[0].update_prompt_raw(text)

    def set_p(self, top_p: float):
        self.top_p = top_p

    def set_k(self, top_k: int):
        self.top_k = top_k

    def set_temp(self, temp: float):
        self.temperature = temp

    def set_max_tokens(self, max_tokens: int):
        self.max_tokens = max_tokens


class AnthropicClaude3Sonnet20240229V1_0Request(AnthropicClaude3SonnetHaikuBaseRequest):
    """
    Anthropic Claude V3 Sonnet model supports temp, top_k, top_p, stop_sequences and max_tokens
    All functionality is implemented in the superclass AnthropicClaude3SonnetHaikuBaseRequest
    """


class AnthropicClaude3Haiku20240307V1_0Request(AnthropicClaude3SonnetHaikuBaseRequest):
    """
    Anthropic Claude V3 Haiku model supports temp, top_k, top_p, stop_sequences and max_tokens
    All functionality is implemented in the superclass AnthropicClaude3SonnetHaikuBaseRequest
    """


class AnthropicClaude3SonnetHaikuBaseResponse(BaseAbstractResponse):
    """
    This class represents the response format used by Anthropic Claude V3 family of models
    Both Haiku and Sonnet use this response format.
    """

    def get_answer(self) -> List[float]:
        return self.result_raw['content'][0]['text']


class AnthropicClaude3Sonnet20240229V1_0Response(AnthropicClaude3SonnetHaikuBaseResponse):
    """
    This class represents the response of Anthropic Claude Vs Sonnet.
    It is implemented in AnthropicClaude3SonnetHaikuBaseResponse
    """


class AnthropicClaude3Haiku20240307V1_0Response(AnthropicClaude3SonnetHaikuBaseResponse):
    """
    This class represents the response of Anthropic Claude V3 Haiku.
    It is implemented in AnthropicClaude3SonnetHaikuBaseResponse
    """
