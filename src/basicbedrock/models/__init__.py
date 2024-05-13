"""
This package contains all models used in basicbedrock.  It models and abstracts all the response/request schemas used by bedrock.
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from .ai21 import *
from .amazon import *
from .anthropic import *
from .baseclasses import BaseAbstractRequest
from .cohere import *
from .meta import *
from .mistral import *

model_request_mapping = {
    "ai21.j2-ultra-v1": AI21Jurassic2BaseRequest,
    "ai21.j2-mid-v1": AI21Jurassic2BaseRequest,
    "amazon.titan-embed-text-v1": AmazonTitanEmbedTextV1Request,
    "amazon.titan-text-lite-v1": AmazonTitanTextG1LiteRequest,
    "amazon.titan-text-express-v1": AmazonTitanTextG1ExpressRequest,
    "anthropic.claude-instant-v1": AnthropicClaudeV1V2BaseRequest,
    "anthropic.claude-v2": AnthropicClaudeV1V2BaseRequest,
    "anthropic.claude-v2:1": AnthropicClaudeV1V2BaseRequest,
    "anthropic.claude-3-sonnet-20240229-v1:0": AnthropicClaude3BaseRequest,
    "anthropic.claude-3-haiku-20240307-v1:0": AnthropicClaude3BaseRequest,
    #  unavailable "anthropic.claude-3-opus-20240229-v1:0":AnthropicClaude3BaseRequest,
    "cohere.command-text-v14": CohereCommandTextBaseRequest,
    "cohere.command-light-text-v14": CohereCommandTextBaseRequest,
    "cohere.embed-english-v3": CohereEmbedBaseRequest,
    "cohere.embed-multilingual-v3": CohereEmbedBaseRequest,
    "cohere.command-r-v1:0": CohereCommandRPLUSTextBaseRequest,
    "cohere.command-r-plus-v1:0": CohereCommandRPLUSTextBaseRequest,
    "meta.llama2-13b-chat-v1": MetaLlamaV2BaseRequest,
    "meta.llama2-70b-chat-v1": MetaLlamaV2BaseRequest,
    "meta.llama3-8b-instruct-v1:0": MetaLlamaV3BaseRequest,
    "meta.llama3-70b-instruct-v1:0": MetaLlamaV3BaseRequest,
    "mistral.mistral-7b-instruct-v0:2": Mistral7BInstructRequest,
    "mistral.mixtral-8x7b-instruct-v0:1": Mistral8X7BInstructRequest,
    "mistral.mistral-large-2402-v1:0": MistralLargeRequest
}

model_response_mapping = {
    "ai21.j2-ultra-v1": AI21Jurassic2BaseResponse,
    "ai21.j2-mid-v1": AI21Jurassic2BaseResponse,
    "amazon.titan-embed-text-v1": AmazonTitanEmbedTextV1Response,
    "amazon.titan-text-lite-v1": AmazonTitanTextV1Response,
    "amazon.titan-text-express-v1": AmazonTitanTextV1Response,
    "anthropic.claude-instant-v1": AnthropicClaudeV1V2BaseResponse,
    "anthropic.claude-v2": AnthropicClaudeV1V2BaseResponse,
    "anthropic.claude-v2:1": AnthropicClaudeV1V2BaseResponse,
    "anthropic.claude-3-sonnet-20240229-v1:0": AnthropicClaude3BaseResponse,
    "anthropic.claude-3-haiku-20240307-v1:0": AnthropicClaude3BaseResponse,
    #  unavailable "anthropic.claude-3-opus-20240229-v1:0": AnthropicClaude3BaseResponse,
    "cohere.command-text-v14": CohereCommandTextBaseResponse,
    "cohere.command-light-text-v14": CohereCommandTextBaseResponse,
    "cohere.embed-english-v3": CohereEmbedBaseResponse,
    "cohere.embed-multilingual-v3": CohereEmbedBaseResponse,
    "cohere.command-r-v1:0": CohereCommandRPLUSTextBaseResponse,
    "cohere.command-r-plus-v1:0": CohereCommandRPLUSTextBaseResponse,
    "meta.llama2-13b-chat-v1": MetaLlamaV2V3BaseResponse,
    "meta.llama2-70b-chat-v1": MetaLlamaV2V3BaseResponse,
    "meta.llama3-8b-instruct-v1:0": MetaLlamaV2V3BaseResponse,
    "meta.llama3-70b-instruct-v1:0":MetaLlamaV2V3BaseResponse,
    "mistral.mistral-7b-instruct-v0:2": MistralBaseResponse,
    "mistral.mixtral-8x7b-instruct-v0:1": MistralBaseResponse,
    "mistral.mistral-large-2402-v1:0": MistralBaseResponse
}


model_request_context_windows = {
    "ai21.j2-ultra-v1": ai21.AI21_JURASSIC2_CONTEXT_WINDOW,
    "ai21.j2-mid-v1": ai21.AI21_JURASSIC2_CONTEXT_WINDOW,
    "amazon.titan-embed-text-v1": None,
    "amazon.titan-text-lite-v1": amazon.AMAZON_TITAN_G1_LITE_CONTEXT_WINDOW,
    "amazon.titan-text-express-v1": amazon.AMAZON_TITAN_G1_EXPRESS_CONTEXT_WINDOW,
    "anthropic.claude-instant-v1": anthropic.ANTHROPIC_CLAUDE_V1V2_CONTEXT_WINDOW,
    "anthropic.claude-v2": anthropic.ANTHROPIC_CLAUDE_V1V2_CONTEXT_WINDOW,
    "anthropic.claude-v2:1": anthropic.ANTHROPIC_CLAUDE_V1V2_CONTEXT_WINDOW,
    "anthropic.claude-3-sonnet-20240229-v1:0": anthropic.ANTHROPIC_CLAUDE_V3_CONTEXT_WINDOW,
    "anthropic.claude-3-haiku-20240307-v1:0": anthropic.ANTHROPIC_CLAUDE_V3_CONTEXT_WINDOW,
    #  unavailable "anthropic.claude-3-opus-20240229-v1:0":AnthropicClaude3BaseRequest,
    "cohere.command-text-v14": cohere.COHERE_COMMAND_TEXT_CONTEXT_WINDOW,
    "cohere.command-light-text-v14": cohere.COHERE_COMMAND_TEXT_CONTEXT_WINDOW,
    "cohere.embed-english-v3": None,
    "cohere.embed-multilingual-v3": None,
    "cohere.command-r-v1:0": COHERE_COMMAND_R_RPLUS_CONTEXT_WINDOW,
    "cohere.command-r-plus-v1:0": COHERE_COMMAND_R_RPLUS_CONTEXT_WINDOW,
    "meta.llama2-13b-chat-v1": meta.META_LLAMA_V2_CONTEXT_WINDOW,
    "meta.llama2-70b-chat-v1": meta.META_LLAMA_V2_CONTEXT_WINDOW,
    "meta.llama3-8b-instruct-v1:0": meta.META_LLAMA_V3_CONTEXT_WINDOW,
    "meta.llama3-70b-instruct-v1:0": meta.META_LLAMA_V3_CONTEXT_WINDOW,
    "mistral.mistral-7b-instruct-v0:2": mistral.MISTRAL_CONTEXT_WINDOW,
    "mistral.mixtral-8x7b-instruct-v0:1": mistral.MISTRAL_CONTEXT_WINDOW,
    "mistral.mistral-large-2402-v1:0": mistral.MISTRAL_CONTEXT_WINDOW
}

model_request_max_outputs = {
    "ai21.j2-ultra-v1": ai21.AI21_JURASSIC2_CONTEXT_WINDOW,
    "ai21.j2-mid-v1": ai21.AI21_JURASSIC2_CONTEXT_WINDOW,
    "amazon.titan-embed-text-v1": None,
    "amazon.titan-text-lite-v1": amazon.AMAZON_TITAN_G1_LITE_CONTEXT_WINDOW,
    "amazon.titan-text-express-v1": amazon.AMAZON_TITAN_G1_LITE_CONTEXT_WINDOW,
    "anthropic.claude-instant-v1": anthropic.ANTHROPIC_CLAUDE_MAX_OUTPUT,
    "anthropic.claude-v2": anthropic.ANTHROPIC_CLAUDE_MAX_OUTPUT,
    "anthropic.claude-v2:1": anthropic.ANTHROPIC_CLAUDE_MAX_OUTPUT,
    "anthropic.claude-3-sonnet-20240229-v1:0": anthropic.ANTHROPIC_CLAUDE_MAX_OUTPUT,
    "anthropic.claude-3-haiku-20240307-v1:0": anthropic.ANTHROPIC_CLAUDE_MAX_OUTPUT,
    #  unavailable "anthropic.claude-3-opus-20240229-v1:0":AnthropicClaude3BaseRequest,
    "cohere.command-text-v14": cohere.COHERE_COMMAND_TEXT_MAX_OUTPUT,
    "cohere.command-light-text-v14": cohere.COHERE_COMMAND_TEXT_MAX_OUTPUT,
    "cohere.command-r-v1:0": COHERE_COMMAND_TEXT_MAX_OUTPUT,
    "cohere.command-r-plus-v1:0": COHERE_COMMAND_TEXT_MAX_OUTPUT,
    "cohere.embed-english-v3": None,
    "cohere.embed-multilingual-v3": None,
    "meta.llama2-13b-chat-v1": meta.META_LLAMA_V2V3_MAX_OUTPUT,
    "meta.llama2-70b-chat-v1": meta.META_LLAMA_V2V3_MAX_OUTPUT,
    "meta.llama3-8b-instruct-v1:0": meta.META_LLAMA_V2V3_MAX_OUTPUT,
    "meta.llama3-70b-instruct-v1:0": meta.META_LLAMA_V2V3_MAX_OUTPUT,
    "mistral.mistral-7b-instruct-v0:2": mistral.MISTRAL_7B_INSTRUCT_MAX_OUTPUT,
    "mistral.mixtral-8x7b-instruct-v0:1": mistral.MISTRAL_8X7B_INSTRUCT_MAX_OUTPUT,
    "mistral.mistral-large-2402-v1:0": mistral.MISTRAL_LARGE_MAX_OUTPUT
}