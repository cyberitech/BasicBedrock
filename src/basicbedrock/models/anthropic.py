from typing import List
from baseclasses import BaseAbstractRequest, BaseAbstractResponse


"""
Anthropic Claude Instant V1
"""
class AnthropicClaudeInstantV1Request(BaseAbstractRequest):
    prompt: str = "\n\nHuman: {PROMPT}\n\nAssistant:"
    max_tokens_to_sample: int = 300
    temperature: float = 0.5
    top_k: int = 250
    top_p: float = 1.
    stop_sequences: list = ["\n\nHuman:"]
    anthropic_version: str = "bedrock-2023-05-31"

    def update_prompt(self,text):
        prompt = f"\n\nHuman: {text}\n\nAssistant:"
        self.update_prompt_raw(prompt)

    def update_prompt_raw(self,text):
        self.prompt = text


class AnthropicClaudeInstantV1Response(BaseAbstractResponse):
    def get_answer(self)->List[float]:
        return self.result_raw['completion']



"""
Anthropic Claude V2
"""
class AnthropicClaudeV2Request(BaseAbstractRequest):
    prompt: str = "\n\nHuman: {PROMPT}\n\nAssistant:"
    max_tokens_to_sample: int = 300
    temperature: float = 0.5
    top_k: int = 250
    top_p: float = 1.
    stop_sequences: list = ["\n\nHuman:"]
    anthropic_version: str = "bedrock-2023-05-31"

    def update_prompt(self,text):
        prompt = f"\n\nHuman: {text}\n\nAssistant:"
        self.update_prompt_raw(prompt)

    def update_prompt_raw(self,text):
        self.prompt = text

class AnthropicClaudeV2Response(BaseAbstractResponse):
    def get_answer(self)->List[float]:
        return self.result_raw['completion']


"""
Anthropic Claude V2:1
"""
class AnthropicClaudeV2_1Request(BaseAbstractRequest):
    prompt: str = "\n\nHuman: {PROMPT}\n\nAssistant:"
    max_tokens_to_sample: int = 300
    temperature: float = 0.5
    top_k: int = 250
    top_p: float = 1.
    stop_sequences: list = ["\n\nHuman:"]
    anthropic_version: str = "bedrock-2023-05-31"

    def update_prompt(self,text):
        prompt = f"\n\nHuman: {text}\n\nAssistant:"
        self.update_prompt_raw(prompt)

    def update_prompt_raw(self,text):
        self.prompt = text

class AnthropicClaudeV2_1Response(BaseAbstractResponse):
    def get_answer(self)->List[float]:
        return self.result_raw['completion']



class AntropicClaude3MessageContent(BaseAbstractRequest):
    type:str = "text"
    text:str = '\n\nHuman: {PROMPT}\n\nAssistant:'

    def update_prompt(self,text):
        text = f'\n\nHuman: {text}\n\nAssistant:'
        self.update_prompt_raw(text)

    def update_prompt_raw(self,text):
        self.text = text

class AntropicClaude3Message(BaseAbstractRequest):
    role:str = "user"
    content: List[AntropicClaude3MessageContent] = [AntropicClaude3MessageContent()]

    def update_prompt(self,text):
        self.content[0].update_prompt(text)

    def update_prompt_raw(self,text):
        self.content[0].update_prompt_raw(text)



"""
Anthropic Claude 3 Sonnet
"""
class AnthropicClaude3Sonnet20240229V1_0Request(BaseAbstractRequest):
    max_tokens: int = 300
    messages: List[AntropicClaude3Message] = [AntropicClaude3Message()]
    anthropic_version: str = "bedrock-2023-05-31"

    def update_prompt(self, text):
        self.messages[0].update_prompt(text)

    def update_prompt_raw(self, text):
        self.messages[0].update_prompt_raw(text)

class AnthropicClaude3Sonnet20240229V1_0Response(BaseAbstractResponse):
    def get_answer(self)->List[float]:
        return self.result_raw['content'][0]['text']


"""
Anthropic Claude 3 Haiku
"""
class AnthropicClaude3Haiku20240307V1_0Request(BaseAbstractRequest):
    max_tokens: int = 300
    messages: List[AntropicClaude3Message] = [AntropicClaude3Message()]
    anthropic_version: str = "bedrock-2023-05-31"

    def update_prompt(self, text):
        self.messages[0].update_prompt(text)

    def update_prompt_raw(self, text):
        self.messages[0].update_prompt_raw(text)

class AnthropicClaude3Haiku20240307V1_0Response(BaseAbstractResponse):
    def get_answer(self)->List[float]:
        return self.result_raw['content'][0]['text']