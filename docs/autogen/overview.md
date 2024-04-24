<!-- markdownlint-disable -->

# API Overview

## Modules

- [`basicbedrock`](./basicbedrock.md#module-basicbedrock): the basicbedrock module contains basicbedrock.BasicBedrock, the top-level class for all of the module's functionality.
- [`basicbedrock.basicbedrock`](./basicbedrock.basicbedrock.md#module-basicbedrockbasicbedrock): Basic Bedrock Python API abstraction.
- [`basicbedrock.models`](./basicbedrock.models.md#module-basicbedrockmodels): This package contains all models used in basicbedrock.  It models and abstracts all the response/request schemas used by bedrock.
- [`basicbedrock.models.ai21`](./basicbedrock.models.ai21.md#module-basicbedrockmodelsai21): File containing all of the definitions and implementations for the AI21 (jurassic) family of requests and responses.
- [`basicbedrock.models.amazon`](./basicbedrock.models.amazon.md#module-basicbedrockmodelsamazon): File containing all of the definitions and implementations for the Amazon family of requests and responses.
- [`basicbedrock.models.anthropic`](./basicbedrock.models.anthropic.md#module-basicbedrockmodelsanthropic): File containing all of the definitions and implementations for the Anthropic family of requests and responses.
- [`basicbedrock.models.baseclasses`](./basicbedrock.models.baseclasses.md#module-basicbedrockmodelsbaseclasses): File containing the base classes used for all model requests and responses.
- [`basicbedrock.models.cohere`](./basicbedrock.models.cohere.md#module-basicbedrockmodelscohere): File containing all of the definitions and implementations for the Cohere family of requests and responses.
- [`basicbedrock.models.meta`](./basicbedrock.models.meta.md#module-basicbedrockmodelsmeta): File containing all of the definitions and implementations for the Meta family of requests and responses.
- [`basicbedrock.models.mistral`](./basicbedrock.models.mistral.md#module-basicbedrockmodelsmistral): File containing all of the definitions and implementations for the Mistral family of requests and responses.

## Classes

- [`basicbedrock.BasicBedrock`](./basicbedrock.basicbedrock.md#class-basicbedrock)
- [`ai21.AI21Jurassic2BaseRequest`](./basicbedrock.models.ai21.md#class-ai21jurassic2baserequest): AI21 Jurassic 2 request format.
- [`ai21.AI21Jurassic2BaseResponse`](./basicbedrock.models.ai21.md#class-ai21jurassic2baseresponse): All AI21 Jurassic 2 models use the same response format.
- [`amazon.AmazonTitanEmbedTextV1Request`](./basicbedrock.models.amazon.md#class-amazontitanembedtextv1request): Request structure for Amazon Titan Embedding V1 API
- [`amazon.AmazonTitanEmbedTextV1Response`](./basicbedrock.models.amazon.md#class-amazontitanembedtextv1response): Response structure for Amazon Titan Embedding V1 API both Express and Lite
- [`amazon.AmazonTitanTextGenerationConfig`](./basicbedrock.models.amazon.md#class-amazontitantextgenerationconfig): Stub class for the configuration blob included as part of requests to Amazon Titan family models.
- [`amazon.AmazonTitanTextV1Request`](./basicbedrock.models.amazon.md#class-amazontitantextv1request): All current Amazon Titan family models use the same request schema.
- [`amazon.AmazonTitanTextV1Response`](./basicbedrock.models.amazon.md#class-amazontitantextv1response): Response structure for Amazon Titan Text V1 API both Express and Lite
- [`anthropic.AnthropicClaude3BaseRequest`](./basicbedrock.models.anthropic.md#class-anthropicclaude3baserequest): This class represents the request format used by Anthropic Claude V3 family of models
- [`anthropic.AnthropicClaude3BaseResponse`](./basicbedrock.models.anthropic.md#class-anthropicclaude3baseresponse): This class represents the response format used by Anthropic Claude V3 family of models
- [`anthropic.AnthropicClaudeV1V2BaseRequest`](./basicbedrock.models.anthropic.md#class-anthropicclaudev1v2baserequest): Claude V1 and V2 family models all utilize the same request/response format
- [`anthropic.AnthropicClaudeV1V2BaseResponse`](./basicbedrock.models.anthropic.md#class-anthropicclaudev1v2baseresponse): Claude V1 and V2 family models all utilize the same response/response format
- [`anthropic.AntropicClaude3Message`](./basicbedrock.models.anthropic.md#class-antropicclaude3message): Stub class for the Antropic Claude V3 message content field.
- [`anthropic.AntropicClaude3MessageContent`](./basicbedrock.models.anthropic.md#class-antropicclaude3messagecontent): Stub class for the Antropic Claude V3 message content field.
- [`baseclasses.BaseAbstractRequest`](./basicbedrock.models.baseclasses.md#class-baseabstractrequest): Abstract base class for all model requests. All model requests must inherit this class.
- [`baseclasses.BaseAbstractResponse`](./basicbedrock.models.baseclasses.md#class-baseabstractresponse): This is the abstract base model for all model responses.
- [`baseclasses.Hyperparams`](./basicbedrock.models.baseclasses.md#class-hyperparams): Hyperparameters for a model.
- [`cohere.CohereCommandTextBaseRequest`](./basicbedrock.models.cohere.md#class-coherecommandtextbaserequest): This is the base request format that all Cohere text-family models use
- [`cohere.CohereCommandTextBaseResponse`](./basicbedrock.models.cohere.md#class-coherecommandtextbaseresponse): this is the base response format used by all text-family cohere models
- [`cohere.CohereEmbedBaseRequest`](./basicbedrock.models.cohere.md#class-cohereembedbaserequest): All cohere command models use the same request format.
- [`cohere.CohereEmbedBaseResponse`](./basicbedrock.models.cohere.md#class-cohereembedbaseresponse): All Cohere Embed models use the same response format.
- [`meta.MetaLlamaV2V3BaseRequest`](./basicbedrock.models.meta.md#class-metallamav2v3baserequest): Meta LLama 2 13b chat request format.
- [`meta.MetaLlamaV2V3BaseResponse`](./basicbedrock.models.meta.md#class-metallamav2v3baseresponse): Response format of Meta Llama 2 V1 family chat response.
- [`mistral.MistralBaseRequest`](./basicbedrock.models.mistral.md#class-mistralbaserequest): Base request for Mistral family of models.
- [`mistral.MistralBaseResponse`](./basicbedrock.models.mistral.md#class-mistralbaseresponse): Base response format for Mistral Instruct family of models.

## Functions

- No functions


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
