from typing import List,Optional
from pydantic import BaseModel
from .baseclasses import BaseAbstractRequest, BaseAbstractResponse


"""
Mistral 7b Instruct V0:2
"""
class MistralMistral7bInstructV0_2Request(BaseAbstractRequest):
    prompt: str = "<s>[INST] this is where you place your input text [/INST]"
    max_tokens: int = 250
    temperature: float = 0.5
    top_p: float = 0.5
    top_k:int = 125

    def update_prompt(self,text):
        input_text = "<s>[INST] {PROMPT} [/INST]"
        input_text = input_text.format(PROMPT=text)
        self.update_prompt_raw(input_text)

    def update_prompt_raw(self,text):
        self.prompt = text

class MistralMistral7bInstructV0_2Response(BaseAbstractResponse):
    def get_answer(self)->str:
        return self.result_raw['outputs'][0]['text']


"""
Mistral 8x7b Instruct V0:1
"""
class MistralMistral8x7bInstructV0_1Request(BaseAbstractRequest):
    prompt: str = "<s>[INST] this is where you place your input text [/INST]"
    max_tokens: int = 250
    temperature: float = 0.5
    top_p: float = 0.5
    top_k:int = 125

    def update_prompt(self,text):
        input_text = "<s>[INST] {PROMPT} [/INST]"
        input_text = input_text.format(PROMPT=text)
        self.update_prompt_raw(input_text)

    def update_prompt_raw(self,text):
        self.prompt = text

class MistralMistral8x7bInstructV0_1Response(BaseAbstractResponse):
    def get_answer(self)->str:
        return self.result_raw['outputs'][0]['text']


"""
Mistral Large 2402 v1:0
"""
class MistralMistralLarge2402V1_0Request(BaseAbstractRequest):
    prompt: str = "<s>[INST] this is where you place your input text [/INST]"
    max_tokens: int = 250
    temperature: float = 0.5
    top_p: float = 0.5
    top_k:int = 125

    def update_prompt(self,text):
        input_text = "<s>[INST] {PROMPT} [/INST]"
        input_text = input_text.format(PROMPT=text)
        self.update_prompt_raw(input_text)

    def update_prompt_raw(self,text):
        self.prompt = text

class MistralMistralLarge2402V1_0Response(BaseAbstractResponse):
    def get_answer(self)->str:
        return self.result_raw['outputs'][0]['text']