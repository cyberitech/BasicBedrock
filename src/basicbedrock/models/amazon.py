from typing import List,Optional
from pydantic import BaseModel
from .baseclasses import BaseAbstractRequest, BaseAbstractResponse



class AmazonTitanTextGenerationConfig(BaseModel):
    maxTokenCount:int = 1000
    stopSequences: List[Optional[str]] = []
    temperature: int = 0.5
    topP: float = 1.


"""
Amazon Titan Embed Text
"""

class AmazonTitanEmbedTextV1Request(BaseAbstractRequest):
    inputText: str = "{PROMPT}"

    def update_prompt(self,text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        self.update_prompt_raw(input_text)

    def update_prompt_raw(self,text):
        self.inputText = text

class AmazonTitanEmbedTextV1Response(BaseAbstractResponse):

    def get_answer(self)->List[float]:
        return self.result_raw['embedding']



"""
Amazon Titan Text Express V1
"""
class AmazonTitanTextExpressV1Request(BaseAbstractRequest):
    inputText: str = "{PROMPT}"
    textGenerationConfig: AmazonTitanTextGenerationConfig = AmazonTitanTextGenerationConfig()

    def update_prompt(self,text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        self.update_prompt_raw(input_text)

    def update_prompt_raw(self,text):
        self.inputText = text


class AmazonTitanTextExpressV1Response(BaseAbstractResponse):

    def get_answer(self)->str:
        return self.result_raw['results'][0]['outputText']



"""
Amazon Titan Text Lite V1
"""
class AmazonTitanTextLiteV1Request(BaseAbstractRequest):
    inputText: str = "{PROMPT}"
    textGenerationConfig: AmazonTitanTextGenerationConfig = AmazonTitanTextGenerationConfig()

    def update_prompt(self,text):
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        self.update_prompt_raw(input_text)

    def update_prompt_raw(self,text):
        self.inputText = text


class AmazonTitanTextLiteV1Response(BaseAbstractResponse):

    def get_answer(self)->str:
        return self.result_raw['results'][0]['outputText']