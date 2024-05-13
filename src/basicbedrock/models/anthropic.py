"""
File containing all of the definitions and implementations for the Anthropic family of requests and responses.
"""
import typing
from typing import List

from pydantic import BaseModel

from baseclasses import BaseAbstractRequest, BaseAbstractResponse


ANTHROPIC_CLAUDE_V1V2_CONTEXT_WINDOW = 100_000 - 1
ANTHROPIC_CLAUDE_V3_CONTEXT_WINDOW = 200_000 - 1
ANTHROPIC_CLAUDE_MAX_OUTPUT = 4_096


class AnthropicClaudeV1V2BaseRequest(BaseAbstractRequest):
    """
    Claude V1 and V2 family models all utilize the same request/response format
    This handles all the logic for them
    this model supports temp, top_k, top_p, stop sequences and max_tokens
    """
    prompt: str = "\n\nHuman: {PROMPT}\n\nAssistant:"
    max_tokens_to_sample: int = 250
    temperature: float = 0.5
    top_k: int = 125
    top_p: float = 0.5
    stop_sequences: list = ["\n\nHuman:"]
    anthropic_version: str = "bedrock-2023-05-31"

    def get_prompt(self) -> str:
        return self.prompt

    def set_prompt(self, text):
        prompt = "\n\nHuman: {PROMPT}\n\nAssistant:"
        padding = len(prompt.replace("{PROMPT}",""))
        cut_text = text[:ANTHROPIC_CLAUDE_V1V2_CONTEXT_WINDOW-padding]
        prompt = prompt.format(PROMPT=cut_text)
        self.set_prompt_raw(prompt)

    def set_prompt_raw(self, text):
        self.prompt = text

    def set_stop_words(self, stop_sequences: List[str]):
        """
        Anthropic Claude V1 and V2 seems to accept any number of stop sequences of any format
        :param stop_sequences: the stop sequences to use
        :return:
        """
        self.stop_sequences = stop_sequences

    def set_p(self, top_p: float):
        self.top_p = top_p

    def set_k(self, top_k: int):
        self.top_k = top_k

    def set_temp(self, temp: float):
        self.temperature = temp

    def set_max_tokens(self, max_tokens: int):
        self.max_tokens_to_sample = min(max_tokens, ANTHROPIC_CLAUDE_MAX_OUTPUT)


class AnthropicClaudeV1V2BaseResponse(BaseAbstractResponse):
    """
    Claude V1 and V2 family models all utilize the same response/response format
    Every Calude V1 and V2 model response will inherit this class
    """

    def get_answer(self) -> List[float]:
        return self.result_raw['completion']


class AntropicClaude3MessageContent(BaseModel):
    """
    Stub class for the Antropic Claude V3 message content field.
    it contains information about the content of the input (is it text or image) as well as the input itself
    """
    type: str = "text"
    text: str = '\n\nHuman: {PROMPT}\n\nAssistant:'

    def update_prompt(self, text):
        prompt = "\n\nHuman: {PROMPT}\n\nAssistant:"
        padding = len(prompt.replace("{PROMPT}",""))
        cut_text = text[:ANTHROPIC_CLAUDE_V1V2_CONTEXT_WINDOW-padding]
        prompt = prompt.format(PROMPT=cut_text)
        self.update_prompt_raw(prompt)

    def update_prompt_raw(self, text):
        self.text = text[:ANTHROPIC_CLAUDE_V3_CONTEXT_WINDOW]


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


class AnthropicClaude3BaseRequest(BaseAbstractRequest):
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
    stop_sequences: List[str] = []

    def get_prompt(self) -> str:
        return self.messages[0].content[0].text

    def set_prompt(self, text):
        self.messages[0].update_prompt(text)

    def set_prompt_raw(self, text):
        self.messages[0].update_prompt_raw(text)

    def set_stop_words(self, stop_sequences: List[str]):
        """
        Anthropic Claude V3 seems to accept any number of stop sequences of any format
        :param stop_sequences: the stop sequences to use
        :return:
        """
        self.stop_sequences = stop_sequences

    def set_p(self, top_p: float):
        self.top_p = top_p

    def set_k(self, top_k: int):
        self.top_k = top_k

    def set_temp(self, temp: float):
        self.temperature = temp

    def set_max_tokens(self, max_tokens: int):
        self.max_tokens = min(max_tokens, ANTHROPIC_CLAUDE_MAX_OUTPUT)


class AnthropicClaude3BaseResponse(BaseAbstractResponse):
    """
    This class represents the response format used by Anthropic Claude V3 family of models
    Both Haiku and Sonnet use this response format.
    """

    def get_answer(self) -> List[float]:
        return self.result_raw['content'][0]['text']
