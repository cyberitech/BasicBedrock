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
    "amazon.titan-text-lite-v1": AmazonTitanTextV1Request,
    "amazon.titan-text-express-v1": AmazonTitanTextV1Request,
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
    "meta.llama2-13b-chat-v1": MetaLlama2ChatV1BaseRequest,
    "meta.llama2-70b-chat-v1": MetaLlama2ChatV1BaseRequest,
    "mistral.mistral-7b-instruct-v0:2": MistralBaseRequest,
    "mistral.mixtral-8x7b-instruct-v0:1": MistralBaseRequest,
    "mistral.mistral-large-2402-v1:0": MistralBaseRequest
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
    "meta.llama2-13b-chat-v1": MetaLlama2ChatV1BaseResponse,
    "meta.llama2-70b-chat-v1": MetaLlama2ChatV1BaseResponse,
    "mistral.mistral-7b-instruct-v0:2": MistralBaseResponse,
    "mistral.mixtral-8x7b-instruct-v0:1": MistralBaseResponse,
    "mistral.mistral-large-2402-v1:0": MistralBaseResponse
}
