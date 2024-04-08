<!-- markdownlint-disable -->

# API Overview

## Modules

- [`basicbedrock`](./basicbedrock.md#module-basicbedrock)
- [`basicbedrock.basicbedrock`](./basicbedrock.basicbedrock.md#module-basicbedrockbasicbedrock): Basic Bedrock Python API abstraction.
- [`basicbedrock.models`](./basicbedrock.models.md#module-basicbedrockmodels)
- [`basicbedrock.models.amazon`](./basicbedrock.models.amazon.md#module-basicbedrockmodelsamazon)
- [`basicbedrock.models.anthropic`](./basicbedrock.models.anthropic.md#module-basicbedrockmodelsanthropic)
- [`basicbedrock.models.baseclasses`](./basicbedrock.models.baseclasses.md#module-basicbedrockmodelsbaseclasses)
- [`basicbedrock.models.cohere`](./basicbedrock.models.cohere.md#module-basicbedrockmodelscohere)
- [`basicbedrock.models.meta`](./basicbedrock.models.meta.md#module-basicbedrockmodelsmeta)
- [`basicbedrock.models.mistral`](./basicbedrock.models.mistral.md#module-basicbedrockmodelsmistral)

## Classes

- [`basicbedrock.BasicBedrock`](./basicbedrock.basicbedrock.md#class-basicbedrock)
- [`amazon.AmazonTitanBaseModelRequest`](./basicbedrock.models.amazon.md#class-amazontitanbasemodelrequest): All current Amazon Titan family models use the same request schema.
- [`amazon.AmazonTitanEmbedTextV1Request`](./basicbedrock.models.amazon.md#class-amazontitanembedtextv1request): Request structure for Amazon Titan Embedding V1 API
- [`amazon.AmazonTitanEmbedTextV1Response`](./basicbedrock.models.amazon.md#class-amazontitanembedtextv1response): Response structure for Amazon Titan Embedding V1 API both Express and Lite
- [`amazon.AmazonTitanTextExpressV1Request`](./basicbedrock.models.amazon.md#class-amazontitantextexpressv1request): Request structure for Amazon Titan Text Express V1 API.
- [`amazon.AmazonTitanTextExpressV1Response`](./basicbedrock.models.amazon.md#class-amazontitantextexpressv1response): Response structure for Amazon Titan Text Express V1 API.
- [`amazon.AmazonTitanTextGenerationConfig`](./basicbedrock.models.amazon.md#class-amazontitantextgenerationconfig): Stub class for the configuration blob included as part of requests to Amazon Titan family models.
- [`amazon.AmazonTitanTextLiteV1Request`](./basicbedrock.models.amazon.md#class-amazontitantextlitev1request): Request structure for Amazon Titan Text Lite V1 API
- [`amazon.AmazonTitanTextLiteV1Response`](./basicbedrock.models.amazon.md#class-amazontitantextlitev1response): Response structure for Amazon Titan Text Lite V1 API.
- [`amazon.AmazonTitanTextV1Response`](./basicbedrock.models.amazon.md#class-amazontitantextv1response): Response structure for Amazon Titan Text V1 API both Express and Lite
- [`anthropic.AnthropicClaude3Haiku20240307V1_0Request`](./basicbedrock.models.anthropic.md#class-anthropicclaude3haiku20240307v1_0request): Anthropic Claude V3 Haiku model supports temp, top_k, top_p, stop_sequences and max_tokens
- [`anthropic.AnthropicClaude3Haiku20240307V1_0Response`](./basicbedrock.models.anthropic.md#class-anthropicclaude3haiku20240307v1_0response): This class represents the response of Anthropic Claude V3 Haiku.
- [`anthropic.AnthropicClaude3Sonnet20240229V1_0Request`](./basicbedrock.models.anthropic.md#class-anthropicclaude3sonnet20240229v1_0request): Anthropic Claude V3 Sonnet model supports temp, top_k, top_p, stop_sequences and max_tokens
- [`anthropic.AnthropicClaude3Sonnet20240229V1_0Response`](./basicbedrock.models.anthropic.md#class-anthropicclaude3sonnet20240229v1_0response): This class represents the response of Anthropic Claude Vs Sonnet.
- [`anthropic.AnthropicClaude3SonnetHaikuBaseRequest`](./basicbedrock.models.anthropic.md#class-anthropicclaude3sonnethaikubaserequest): This class represents the request format used by Anthropic Claude V3 family of models
- [`anthropic.AnthropicClaude3SonnetHaikuBaseResponse`](./basicbedrock.models.anthropic.md#class-anthropicclaude3sonnethaikubaseresponse): This class represents the response format used by Anthropic Claude V3 family of models
- [`anthropic.AnthropicClaudeInstantV1Request`](./basicbedrock.models.anthropic.md#class-anthropicclaudeinstantv1request): Anthropic Claude Instant V1 model supports temp, top_k, top_p, stop_sequences and max_tokens
- [`anthropic.AnthropicClaudeInstantV1Response`](./basicbedrock.models.anthropic.md#class-anthropicclaudeinstantv1response): The class representing the response of Anthropic Claude Instant V1 model
- [`anthropic.AnthropicClaudeV1V2BaseModelResponse`](./basicbedrock.models.anthropic.md#class-anthropicclaudev1v2basemodelresponse): Claude V1 and V2 family models all utilize the same response/response format
- [`anthropic.AnthropicClaudeV2Request`](./basicbedrock.models.anthropic.md#class-anthropicclaudev2request): Anthropic Claude V2 model supports temp, top_k, top_p, stop_sequences and max_tokens
- [`anthropic.AnthropicClaudeV2Response`](./basicbedrock.models.anthropic.md#class-anthropicclaudev2response): The class representing the response of Anthropic Claude V2 model
- [`anthropic.AnthropicClaudeV2_1Request`](./basicbedrock.models.anthropic.md#class-anthropicclaudev2_1request): Anthropic Claude V2:1 model supports temp, top_k, top_p, stop_sequences and max_tokens
- [`anthropic.AnthropicClaudeV2_1Response`](./basicbedrock.models.anthropic.md#class-anthropicclaudev2_1response): The class representing the response of Anthropic Claude V2:1 model
- [`anthropic.AnthropicV1V2BaseModelRequest`](./basicbedrock.models.anthropic.md#class-anthropicv1v2basemodelrequest): Claude V1 and V2 family models all utilize the same request/response format
- [`anthropic.AntropicClaude3Message`](./basicbedrock.models.anthropic.md#class-antropicclaude3message): Stub class for the Antropic Claude V3 message content field.
- [`anthropic.AntropicClaude3MessageContent`](./basicbedrock.models.anthropic.md#class-antropicclaude3messagecontent): Stub class for the Antropic Claude V3 message content field.
- [`baseclasses.BaseAbstractRequest`](./basicbedrock.models.baseclasses.md#class-baseabstractrequest): Abstract base class for all model requests. All model requests must inherit this class.
- [`baseclasses.BaseAbstractResponse`](./basicbedrock.models.baseclasses.md#class-baseabstractresponse): This is the abstract base model for all model responses.
- [`baseclasses.Hyperparams`](./basicbedrock.models.baseclasses.md#class-hyperparams): Hyperparameters for a model.
- [`cohere.CohereCommandBaseRequest`](./basicbedrock.models.cohere.md#class-coherecommandbaserequest): This is the base request format that all Cohere text-family models use
- [`cohere.CohereCommandLightTextV14Request`](./basicbedrock.models.cohere.md#class-coherecommandlighttextv14request): Cohere Command Light Text V14 supports top_p, top_k, temperature and max_tokens
- [`cohere.CohereCommandLightTextV14Response`](./basicbedrock.models.cohere.md#class-coherecommandlighttextv14response): This is the response format for Cohere Command Light Text v14
- [`cohere.CohereCommandTextBaseResponse`](./basicbedrock.models.cohere.md#class-coherecommandtextbaseresponse): this is the base response format used by all text-family cohere models
- [`cohere.CohereCommandTextV14Request`](./basicbedrock.models.cohere.md#class-coherecommandtextv14request): Cohere Command Text V14 supports top_p, top_k, temperature and max_tokens
- [`cohere.CohereCommandTextV14Response`](./basicbedrock.models.cohere.md#class-coherecommandtextv14response): This is the response format for Cohere Command Text v14
- [`cohere.CohereEmbedBaseRequest`](./basicbedrock.models.cohere.md#class-cohereembedbaserequest): All cohere command models use the same request format.
- [`cohere.CohereEmbedBaseResponse`](./basicbedrock.models.cohere.md#class-cohereembedbaseresponse): All Cohere Embed models use the same response format.
- [`cohere.CohereEmbedEnglishV3Request`](./basicbedrock.models.cohere.md#class-cohereembedenglishv3request): Request for Cohere Embed English V3.
- [`cohere.CohereEmbedEnglishV3Response`](./basicbedrock.models.cohere.md#class-cohereembedenglishv3response): Response format for Cohere Embed English V3
- [`cohere.CohereEmbedMultilingualV3Request`](./basicbedrock.models.cohere.md#class-cohereembedmultilingualv3request): Request for Cohere Embed Multilingual V3.
- [`cohere.CohereEmbedMultilingualV3Response`](./basicbedrock.models.cohere.md#class-cohereembedmultilingualv3response): Response for Cohere Embed Multilingual V3.
- [`meta.MetaLlama213bChatV1Request`](./basicbedrock.models.meta.md#class-metallama213bchatv1request): Request format for Meta Llama 2 13b chat.
- [`meta.MetaLlama213bChatV1Response`](./basicbedrock.models.meta.md#class-metallama213bchatv1response): Response format of Meta Llama 2 13b chat response.
- [`meta.MetaLlama270bChatV1Request`](./basicbedrock.models.meta.md#class-metallama270bchatv1request): Request format for Meta Llama 2 70b chat.
- [`meta.MetaLlama270bChatV1Response`](./basicbedrock.models.meta.md#class-metallama270bchatv1response): Response format of Meta Llama 2 70b chat response.
- [`meta.MetaLlama2ChatV1BaseRequest`](./basicbedrock.models.meta.md#class-metallama2chatv1baserequest): Meta LLama 2 13b chat request format.
- [`meta.MetaLlama2V1BaseResponse`](./basicbedrock.models.meta.md#class-metallama2v1baseresponse): Response format of Meta Llama 2 V1 family chat response.
- [`mistral.MistralBaseRequest`](./basicbedrock.models.mistral.md#class-mistralbaserequest): Base request for Mistral family of models.
- [`mistral.MistralBaseResponse`](./basicbedrock.models.mistral.md#class-mistralbaseresponse): Base response format for Mistral Instruct family of models.
- [`mistral.MistralMistral7bInstructV0_2Request`](./basicbedrock.models.mistral.md#class-mistralmistral7binstructv0_2request): Request format for Mistral 7b Instruct V0:2
- [`mistral.MistralMistral7bInstructV0_2Response`](./basicbedrock.models.mistral.md#class-mistralmistral7binstructv0_2response): Response format for Mistral 7b Instruct V0:2
- [`mistral.MistralMistral8x7bInstructV0_1Request`](./basicbedrock.models.mistral.md#class-mistralmistral8x7binstructv0_1request): Request format for Mistral 8x7b Instruct V0:1
- [`mistral.MistralMistral8x7bInstructV0_1Response`](./basicbedrock.models.mistral.md#class-mistralmistral8x7binstructv0_1response): Response format for Mistral 8x7b Instruct V0:2
- [`mistral.MistralMistralLarge2402V1_0Request`](./basicbedrock.models.mistral.md#class-mistralmistrallarge2402v1_0request): Request format for Mistral Large 2402 V1:0
- [`mistral.MistralMistralLarge2402V1_0Response`](./basicbedrock.models.mistral.md#class-mistralmistrallarge2402v1_0response): Response format for Mistral Large 2402 v1:0

## Functions

- No functions


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
