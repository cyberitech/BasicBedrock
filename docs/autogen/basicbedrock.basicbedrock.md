<!-- markdownlint-disable -->

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/basicbedrock.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `basicbedrock.basicbedrock`
Basic Bedrock Python API abstraction. Currently supports all text-modal foundation models in AWS Bedrock. Abstracts away the need to understand any of the model-specific response or request semantics. Simply pick a model, and invoke it with a prompt. If you with to specify k, p, temp, and max_token parameters, they will be applied on a best effort basis. not all models support all parameters. 

**Global Variables**
---------------
- **AI21_JURASSIC2_CONTEXT_WINDOW**
- **AI21_JURASSIC2_MAX_OUTPUT**
- **AMAZON_TITAN_G1_LITE_CONTEXT_WINDOW**
- **AMAZON_TITAN_G1_EXPRESS_CONTEXT_WINDOW**
- **AMAZON_TITAN_TEXT_MAX_OUTPUT**
- **ANTHROPIC_CLAUDE_V1V2_CONTEXT_WINDOW**
- **ANTHROPIC_CLAUDE_V3_CONTEXT_WINDOW**
- **ANTHROPIC_CLAUDE_MAX_OUTPUT**
- **COHERE_COMMAND_TEXT_CONTEXT_WINDOW**
- **COHERE_COMMAND_R_RPLUS_CONTEXT_WINDOW**
- **COHERE_COMMAND_TEXT_MAX_OUTPUT**
- **COHERE_COMMAND_R_MAX_OUTPUT**
- **COHERE_COMMAND_RPLUS_MAX_OUTPUT**
- **META_LLAMA_V2_CONTEXT_WINDOW**
- **META_LLAMA_V3_CONTEXT_WINDOW**
- **META_LLAMA_V2V3_MAX_OUTPUT**
- **MISTRAL_CONTEXT_WINDOW**
- **MISTRAL_7B_INSTRUCT_MAX_OUTPUT**
- **MISTRAL_8X7B_INSTRUCT_MAX_OUTPUT**
- **MISTRAL_LARGE_MAX_OUTPUT**
- **model_request_mapping**
- **model_response_mapping**
- **model_request_context_windows**
- **model_request_max_outputs**


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/basicbedrock.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BasicBedrock`




<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/basicbedrock.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(session: Session = None, **kwargs)
```

Creates an instance of basic bedrock. session param is optional.  If omitted, a default session constructor will be used. Right now, the only kwargs supported are a param dictionary. Param dicts are in the format of {'top_p': float, 'top_k': int, 'temp': float, 'max_tokens': int} :param session: the boto3 session to use for creating the basic bedrock instance :param kwargs: kwargs used are in the format of {'top_p': float, 'top_k': int, 'temp': float, 'max_tokens': int} 


---

#### <kbd>property</kbd> max_tokens

returns the max_tokens parameter :return: the int max_tokens parameter 

---

#### <kbd>property</kbd> params

returns the params dictionary :return: params dict in format of {'top_p': float, 'top_k': int, 'temp': float, 'max_tokens': int} 

---

#### <kbd>property</kbd> stop_words

returns the stop_words parameter :return: a list of stop words 

---

#### <kbd>property</kbd> temp

returns the temp parameter :return: a float representing the temperature 

---

#### <kbd>property</kbd> top_k

returns the top_k parameter :return: a int representing the top_k parameter 

---

#### <kbd>property</kbd> top_p

returns the top_p parameter :return: a float representing the top_p parameter 



---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/basicbedrock.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_available_models`

```python
get_available_models()
```

Gets a list of available models that are supported by BasicBedrock and enabled in the aws account :return: list of models both enabled and suported 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/basicbedrock.py#L162"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_boto3_body`

```python
get_boto3_body(model_id: str, prompt: str) → str
```

given a model_id and a prompt, this will construct the boto3 'body' parameter using the specified prompt and params, but it will not invoke bedrock or pass it to boto3, it will simply return the boto3 'body' param as a string. Internally, this calls the update_prompt() function, not update_prompt_raw(), which means that it will take into account the expected calling convention of the underlying model by inserting things such as 'Human:' or '<s>[INST]' as appropriate :param model_id: the model to construct a boto3 body for :param prompt: the prompt to pass the model. :return: a string, representing the equivalent boto3 'body' parameter. 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/basicbedrock.py#L127"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_model_request_json`

```python
get_model_request_json(model_id: str) → str
```

returns a string object representing the request scheme of model_id in json format :param model_id:  the chosen model id :return: a json string 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/basicbedrock.py#L113"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_model_request_object`

```python
get_model_request_object(model_id: str) → BaseAbstractRequest
```

returns an instantiated object representing the schema for the chosen model. All these inherit from BaseSchemaAbstract. Its useful for when you want to use BaseSchemaAbstract to modify prompts and produce json or dicts manually :param model_id: the chosen model ID :return: the schema class object for the chosen model, it will be a subclass of a BaseAbstractRequest 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/basicbedrock.py#L97"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_model_schema_dict`

```python
get_model_schema_dict(model_id: str) → dict
```

returns a dict object representing the request scheme of model_id :param model_id:  the chosen model id :return: dict object representing the base request scheme of model_id 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/basicbedrock.py#L89"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_supported_models`

```python
get_supported_models() → list
```

returns a list of all models supported by BasicBedrock, which may not be the same models a user has enabled within their account :return: ["model1", "model2", "model3"...] 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/basicbedrock.py#L183"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `invoke`

```python
invoke(
    model_id: str,
    request: Union[str, dict],
    show_request: bool = False,
    guardrail: Guardrails = None
) → BaseAbstractResponse
```

invokes a model_id and returns the response.  Non-streaming only. request may by one of: a prompt, a json string represent the request schema, or a dict representing the request schema invoking with a request of a string containing valid json data, if it is not a valid json schema for the model it will be interpreted as a prompt string and a runtime warning will be raised :param model_id: the model id you wish to invoke :param request: a string or dict representing either a prompt or a model request schema :param: guardrail: Optional instance of a basicbedrock.guardrails.Guardrails class. If present, it will utilize the guardrail within it. :param show_request: prints the request blob before invoking :return: the response to the request, as a subclass of a model.BaseAbstractResponse 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/basicbedrock.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `print_available_models`

```python
print_available_models()
```

Prints available models that are supported by BasicBedrock and enabled in the aws account :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/basicbedrock.py#L143"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `print_model_schema`

```python
print_model_schema(model_id: str, indent: int = None) → None
```

prints the request scheme of model_id in a pretty format. if indent is not None, indent the lines when printing :param model_id: the chosen model id :param indent: how many spaces to indent, default=4 :return: None 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/basicbedrock.py#L81"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `print_supported_models`

```python
print_supported_models() → None
```

Prints all models supported by BasicBedrock, which may not be the same models a user has enabled within their account :return: None 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/basicbedrock.py#L278"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reset_params`

```python
reset_params()
```

resets the params dictionary to default values these values are defined in _default_k, _default_p, _default_t, _default_n :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/basicbedrock.py#L270"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_params`

```python
set_params(params: dict) → None
```

wrapper for property params, allow you to call it as a function :param params: a dict containing any of top_p, top_k, temp, max_tokens :return: 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
