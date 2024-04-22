<!-- markdownlint-disable -->

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `basicbedrock.models.amazon`
File containing all of the definitions and implementations for the Amazon family of requests and responses. 



---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AmazonTitanTextGenerationConfig`
Stub class for the configuration blob included as part of requests to Amazon Titan family models. the available hyperparameters are kept internally here and include P, temperate and max_tokens this model does not support K values. 


---

#### <kbd>property</kbd> model_extra

Get extra fields set during validation. 



**Returns:**
  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. 

---

#### <kbd>property</kbd> model_fields_set

Returns the set of fields that have been explicitly set on this model instance. 



**Returns:**
  A set of strings representing the fields that have been set,  i.e. that were not filled from defaults. 




---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AmazonTitanTextV1Request`
All current Amazon Titan family models use the same request schema. This base class is used by both Amazon Titan Text G1 Express and Titan Text v1 Lite This model does not support top_k parameter. 


---

#### <kbd>property</kbd> model_extra

Get extra fields set during validation. 



**Returns:**
  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. 

---

#### <kbd>property</kbd> model_fields_set

Returns the set of fields that have been explicitly set on this model instance. 



**Returns:**
  A set of strings representing the fields that have been set,  i.e. that were not filled from defaults. 



---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```

Top K is not supported by Amazon Titan model family.  This method does nothing. :param top_k: int :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L78"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```

sets max token output of Amazon Titan model family :param max_tokens: int :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L86"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```

Sets top p of Amazon Titan model family :param top_p: float :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_prompt`

```python
set_prompt(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_prompt_raw`

```python
set_prompt_raw(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_stop_words`

```python
set_stop_words(stop_words: List[str])
```

https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-text.html#model-parameters-titan-request-response Only valid stop words are "|", "User:" or none at all If no valid stop words are passed, the default of [] is used If a valid stop word is present in the list, the first one will be used :param stop_words: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L70"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```

Sets temperature of Amazon Titan model family :param temp: flat :return: 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L96"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AmazonTitanTextV1Response`
Response structure for Amazon Titan Text V1 API both Express and Lite 


---

#### <kbd>property</kbd> model_extra

Get extra fields set during validation. 



**Returns:**
  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. 

---

#### <kbd>property</kbd> model_fields_set

Returns the set of fields that have been explicitly set on this model instance. 



**Returns:**
  A set of strings representing the fields that have been set,  i.e. that were not filled from defaults. 



---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L101"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → List[float]
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L106"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AmazonTitanEmbedTextV1Request`
Request structure for Amazon Titan Embedding V1 API This model accepts text and returns a list of floats, representing Amazon Titan embedding vectors. 


---

#### <kbd>property</kbd> model_extra

Get extra fields set during validation. 



**Returns:**
  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. 

---

#### <kbd>property</kbd> model_fields_set

Returns the set of fields that have been explicitly set on this model instance. 



**Returns:**
  A set of strings representing the fields that have been set,  i.e. that were not filled from defaults. 



---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L124"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```

Top K is not supported by Amazon Titan Embedding V1 API :param top_k: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L140"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```

Sets max token output of Amazon Titan Embedding V1 API :param max_tokens: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L148"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```

Sets top p of Amazon Titan Embedding V1 API :param top_p: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L113"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_prompt`

```python
set_prompt(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_prompt_raw`

```python
set_prompt_raw(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L121"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_stop_words`

```python
set_stop_words(stop_words: List[str])
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L132"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```

Sets temperature of Amazon Titan Embedding V1 API :param temp: :return: 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L157"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AmazonTitanEmbedTextV1Response`
Response structure for Amazon Titan Embedding V1 API both Express and Lite 


---

#### <kbd>property</kbd> model_extra

Get extra fields set during validation. 



**Returns:**
  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. 

---

#### <kbd>property</kbd> model_fields_set

Returns the set of fields that have been explicitly set on this model instance. 



**Returns:**
  A set of strings representing the fields that have been set,  i.e. that were not filled from defaults. 



---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/amazon.py#L162"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → List[float]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
