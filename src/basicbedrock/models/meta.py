from typing import List
from baseclasses import BaseAbstractRequest, BaseAbstractResponse

"""
Amazon docs currently do not have request schemas for Llama 2 13b and Llama 2 70b, only the chat versions
"""


"""
Meta Llama 2 13b Chat V1
"""
class MetaLlama213bChatV1Request(BaseAbstractRequest):
    prompt: str = "{PROMPT}"
    max_gen_len:int = 512
    temperature: float = 0.5
    top_p:float = 0.5

    def update_prompt(self,text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        self.update_prompt_raw(input_text)

    def update_prompt_raw(self,text):
        self.prompt = text

class MetaLlama213bChatV1Response(BaseAbstractResponse):
    def get_answer(self)->str:
        return self.result_raw['generation']


"""
Meta Llama 2 70b Chat V1
"""
class MetaLlama270bChatV1Request(BaseAbstractRequest):
    prompt: str = "{PROMPT}"
    max_gen_len:int = 512
    temperature: float = 0.5
    top_p:float = 0.5

    def update_prompt(self,text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        self.update_prompt_raw(input_text)

    def update_prompt_raw(self,text):
        self.prompt = text

class MetaLlama270bChatV1Response(BaseAbstractResponse):
    def get_answer(self)->str:
        return self.result_raw['generation']