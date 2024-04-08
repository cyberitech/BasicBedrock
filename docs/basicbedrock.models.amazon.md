<!-- markdownlint-disable -->

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `basicbedrock.models.amazon`
File containing all of the definitions and implementations for the Amazon family of requests and responses. 



---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AmazonTitanBaseModelRequest`
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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```

Top K is not supported by Amazon Titan model family.  This method does nothing. :param top_k: int :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```

sets max token output of Amazon Titan model family :param max_tokens: int :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```

Sets top p of Amazon Titan model family :param top_p: float :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```

Sets temperature of Amazon Titan model family :param temp: flat :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(text)
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L73"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AmazonTitanTextExpressV1Request`
Request structure for Amazon Titan Text Express V1 API. This model accepts text and returns text. This model does not support K parameter. 

Please see AmazonTitanBaseModelRequest for the implementation of all methods 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```

Top K is not supported by Amazon Titan model family.  This method does nothing. :param top_k: int :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```

sets max token output of Amazon Titan model family :param max_tokens: int :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```

Sets top p of Amazon Titan model family :param top_p: float :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```

Sets temperature of Amazon Titan model family :param temp: flat :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(text)
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AmazonTitanTextLiteV1Request`
Request structure for Amazon Titan Text Lite V1 API This model accepts text and returns text. This model does not support K parameter. 

Please see AmazonTitanBaseModelRequest for the implementation of all methods 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```

Top K is not supported by Amazon Titan model family.  This method does nothing. :param top_k: int :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```

sets max token output of Amazon Titan model family :param max_tokens: int :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```

Sets top p of Amazon Titan model family :param top_p: float :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```

Sets temperature of Amazon Titan model family :param temp: flat :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(text)
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → List[float]
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AmazonTitanTextExpressV1Response`
Response structure for Amazon Titan Text Express V1 API. Implemented in AmazonTitanTextV1Response 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → List[float]
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L109"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AmazonTitanTextLiteV1Response`
Response structure for Amazon Titan Text Lite V1 API. Implemented in AmazonTitanTextV1Response 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → List[float]
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L131"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```

Top K is not supported by Amazon Titan Embedding V1 API :param top_k: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L147"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```

Sets max token output of Amazon Titan Embedding V1 API :param max_tokens: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```

Sets top p of Amazon Titan Embedding V1 API :param top_p: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L139"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```

Sets temperature of Amazon Titan Embedding V1 API :param temp: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L123"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L128"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(text)
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L164"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\amazon.py#L169"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → List[float]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
