"""
File containing all of the definitions and implementations for the Meta family of requests and responses.
Amazon docs currently do not have request schemas for Llama 2 13b and Llama 2 70b, only the chat versions
"""
from baseclasses import BaseAbstractRequest, BaseAbstractResponse


class MetaLlama2ChatV1BaseRequest(BaseAbstractRequest):
    """
    Meta LLama 2 13b chat request format.
    This model supports max_token, temperature and top_p.
    It does not support top_k
    """
    prompt: str = "{PROMPT}"
    max_gen_len: int = 512
    temperature: float = 0.5
    top_p: float = 0.5

    def update_prompt(self, text):
        """
        Update the prompt based on the input text.
        inserts text according to expected request conventions.
        :param text:
        :return:
        """
        input_text = "{PROMPT}"
        input_text = input_text.format(PROMPT=text)
        self.update_prompt_raw(input_text)

    def update_prompt_raw(self, text):
        """
        Update the prompt based on the input text without regards to expected input format
        what you insert, is inserted raw without formatting
        :param text:
        :return:
        """
        self.prompt = text

    def set_p(self, top_p: float):
        """
        Set the top_p parameter.
        :param top_p:
        :return:
        """
        self.top_p = top_p

    def set_k(self, top_k: int):
        """
        This model does not support top_k
        :param top_k:
        :return:
        """
        pass

    def set_temp(self, temp: float):
        """
        set the temperature parameter.
        :param temp:
        :return:
        """
        self.temperature = temp

    def set_max_tokens(self, max_tokens: int):
        """
        set the maximum tokens parameter.
        :param max_tokens:
        :return:
        """
        self.max_gen_len = max_tokens


class MetaLlama213bChatV1Request(MetaLlama2ChatV1BaseRequest):
    """
    Request format for Meta Llama 2 13b chat.
    this model supports max_token, temperature and top_p.
    It does not support top_k
    This class is implemented in MetaLlama2ChatV1BaseRequest.
    """


class MetaLlama270bChatV1Request(MetaLlama2ChatV1BaseRequest):
    """
    Request format for Meta Llama 2 70b chat.
    this model supports max_token, temperature and top_p.
    It does not support top_k
    This class is implemented in MetaLlama2ChatV1BaseRequest.
    """


class MetaLlama2V1BaseResponse(BaseAbstractResponse):
    """
    Response format of Meta Llama 2 V1 family chat response.
    """

    def get_answer(self) -> str:
        return self.result_raw['generation']


class MetaLlama213bChatV1Response(MetaLlama2V1BaseResponse):
    """
    Response format of Meta Llama 2 13b chat response.
    Implemented in MetaLlama2V1BaseResponse.
    """


class MetaLlama270bChatV1Response(MetaLlama2V1BaseResponse):
    """
    Response format of Meta Llama 2 70b chat response.
    Implemented in MetaLlama2V1BaseResponse.
    """
