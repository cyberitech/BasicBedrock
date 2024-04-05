from typing import List
from baseclasses import BaseAbstractRequest,BaseAbstractResponse


"""
Cohere Command Text V14
"""
class CohereCommandTextV14Request(BaseAbstractRequest):
    prompt: str = "{PROMPT}"
    max_tokens:int = 1000
    temperature: float = 0.5
    p:float = 0.5
    k:int = 125

    def update_prompt(self,text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        self.update_prompt_raw(input_text)

    def update_prompt_raw(self,text):
        self.prompt = text

class CohereCommandTextV14Response(BaseAbstractResponse):
    def get_answer(self)->str:
        return self.result_raw['generations'][0]['text']




"""
Cohere Command Light Text V14
"""
class CohereCommandLightTextV14Request(BaseAbstractRequest):
    prompt: str = "{PROMPT}"
    max_tokens: int = 1000
    temperature: float = 0.5

    def update_prompt(self, text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        self.update_prompt_raw(input_text)

    def update_prompt_raw(self, text):
        self.prompt = text

class CohereCommandLightTextV14Response(BaseAbstractResponse):
    def get_answer(self)->str:
        return self.result_raw['generations'][0]['text']



"""
Cohere Embed English V3
"""
class CohereEmbedEnglishV3Request(BaseAbstractRequest):
    texts: List[str] = ["{PROMPT}"]
    input_type: str = "search_document"

    def update_prompt(self, text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        texts = [input_text]
        self.update_prompt_raw(texts)

    def update_prompt_raw(self, texts:list):
        self.texts = texts

class CohereEmbedEnglishV3Response(BaseAbstractResponse):
    def get_answer(self)->List[float]:
        return self.result_raw['embeddings'][0]



"""
Cohere Embed Multilingual V3
"""
class CohereEmbedMultilingualV3Request(BaseAbstractRequest):
    texts: List[str] = ["{PROMPT}"]
    input_type: str = "search_document"

    def update_prompt(self, text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        texts = [input_text]
        self.update_prompt_raw(texts)

    def update_prompt_raw(self, texts:list):
        self.texts = texts

class CohereEmbedMultilingualV3Response(BaseAbstractResponse):
    def get_answer(self)->List[float]:
        return self.result_raw['embeddings'][0]