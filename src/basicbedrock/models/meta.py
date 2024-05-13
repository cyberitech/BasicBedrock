"""
File containing all of the definitions and implementations for the Meta family of requests and responses.
Amazon docs currently do not have request schemas for Llama 2 13b and Llama 2 70b, only the chat versions
"""
import typing

from baseclasses import BaseAbstractRequest, BaseAbstractResponse


META_LLAMA_V2_CONTEXT_WINDOW = 4_000
META_LLAMA_V3_CONTEXT_WINDOW = 8_000
META_LLAMA_V2V3_MAX_OUTPUT = 2_048


class MetaLlamaBaseRequest(BaseAbstractRequest):
    """
    This model supports max_token, temperature and top_p.
    It does not support top_k
    """

    max_gen_len: int = 250
    temperature: float = 0.5
    top_p: float = 0.5

    def get_prompt(self) -> str:
        pass

    def set_stop_words(self, stop_words: typing.List[str]):
        """
        Meta Llama 2 models dont support stop words
        :param stop_words:
        :return:
        """
        pass

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
        self.max_gen_len = min(max_tokens, META_LLAMA_V2V3_MAX_OUTPUT)

    def set_prompt(self, text: str):
        pass

    def set_prompt_raw(self, text: str):
        pass


class MetaLlamaV2V3BaseResponse(BaseAbstractResponse):
    """
    Response format of Meta Llama 2 V1 family chat response.
    """

    def get_answer(self) -> str:
        return self.result_raw['generation']


class MetaLlamaV2BaseRequest(MetaLlamaBaseRequest):
    """
    Specifies the expected Llama 2 V1 family chat request format using the [INST] tags
    """
    prompt: str = "<s>[INST]{PROMPT}[/INST]"

    def get_prompt(self) -> str:
        return self.prompt

    def set_prompt(self, text):
        prompt = "<s>[INST]{PROMPT}[/INST]"
        padding = len(prompt.replace("{PROMPT}",""))
        cut_text = text[:META_LLAMA_V2_CONTEXT_WINDOW-padding]
        prompt = prompt.format(PROMPT=cut_text)
        self.set_prompt_raw(prompt)

    def set_prompt_raw(self, text):
        """
        Update the prompt based on the input text without regards to expected input format
        what you insert, is inserted raw without formatting
        :param text:
        :return:
        """
        self.prompt = text


class MetaLlamaV3BaseRequest(MetaLlamaBaseRequest):
    """
    Specifies the expected Llama 2 V1 family chat request format using the expected header format
    """
    prompt: str = (
        '<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n'
        '\n'
        '{PROMPT}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n'
    )

    def get_prompt(self) -> str:
        return self.prompt

    def set_prompt(self, text):
        prompt = str(
            "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n"
            "\n"
            "{PROMPT}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n"
        )
        padding = len(prompt.replace("{PROMPT}",""))
        cut_text = text[:META_LLAMA_V3_CONTEXT_WINDOW-padding]
        prompt = prompt.format(PROMPT=cut_text)
        self.set_prompt_raw(prompt)

    def set_prompt_raw(self, text):
        """
        Update the prompt based on the input text without regards to expected input format
        what you insert, is inserted raw without formatting
        :param text:
        :return:
        """
        self.prompt = text
