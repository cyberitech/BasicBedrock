import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from .amazon import *
from .anthropic import *
from .baseclasses import BaseAbstractRequest
from .cohere import *
from .meta import *
from .mistral import *

model_request_mapping = {
    "amazon.titan-embed-text-v1": AmazonTitanEmbedTextV1Request,
    "amazon.titan-text-lite-v1": AmazonTitanTextLiteV1Request,
    "amazon.titan-text-express-v1": AmazonTitanTextExpressV1Request,
    "anthropic.claude-instant-v1": AnthropicClaudeInstantV1Request,
    "anthropic.claude-v2": AnthropicClaudeV2Request,
    "anthropic.claude-v2:1": AnthropicClaudeV2_1Request,
    "anthropic.claude-3-sonnet-20240229-v1:0": AnthropicClaude3Sonnet20240229V1_0Request,
    "anthropic.claude-3-haiku-20240307-v1:0": AnthropicClaude3Haiku20240307V1_0Request,
    "cohere.command-text-v14": CohereCommandTextV14Request,
    "cohere.command-light-text-v14":CohereCommandLightTextV14Request,
    "cohere.embed-english-v3":CohereEmbedEnglishV3Request,
    "cohere.embed-multilingual-v3":CohereEmbedMultilingualV3Request,
    "meta.llama2-13b-chat-v1": MetaLlama213bChatV1Request,
    "meta.llama2-70b-chat-v1": MetaLlama270bChatV1Request,
    "mistral.mistral-7b-instruct-v0:2": MistralMistral7bInstructV0_2Request,
    "mistral.mixtral-8x7b-instruct-v0:1": MistralMistral8x7bInstructV0_1Request,
    "mistral.mistral-large-2402-v1:0":MistralMistralLarge2402V1_0Request
}

model_response_mapping = {
    "amazon.titan-embed-text-v1": AmazonTitanEmbedTextV1Response,
    "amazon.titan-text-lite-v1": AmazonTitanTextLiteV1Response,
    "amazon.titan-text-express-v1": AmazonTitanTextExpressV1Response,
    "anthropic.claude-instant-v1": AnthropicClaudeInstantV1Response,
    "anthropic.claude-v2": AnthropicClaudeV2Response,
    "anthropic.claude-v2:1": AnthropicClaudeV2_1Response,
    "anthropic.claude-3-sonnet-20240229-v1:0": AnthropicClaude3Sonnet20240229V1_0Response,
    "anthropic.claude-3-haiku-20240307-v1:0": AnthropicClaude3Haiku20240307V1_0Response,
    "cohere.command-text-v14": CohereCommandTextV14Response,
    "cohere.command-light-text-v14":CohereCommandLightTextV14Response,
    "cohere.embed-english-v3":CohereEmbedEnglishV3Response,
    "cohere.embed-multilingual-v3":CohereEmbedMultilingualV3Response,
    "meta.llama2-13b-chat-v1": MetaLlama213bChatV1Response,
    "meta.llama2-70b-chat-v1": MetaLlama270bChatV1Response,
    "mistral.mistral-7b-instruct-v0:2": MistralMistral7bInstructV0_2Response,
    "mistral.mixtral-8x7b-instruct-v0:1": MistralMistral8x7bInstructV0_1Response,
    "mistral.mistral-large-2402-v1:0":MistralMistralLarge2402V1_0Response
}