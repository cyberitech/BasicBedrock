<!-- markdownlint-disable -->

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `basicbedrock.models.cohere`






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L5"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CohereCommandBaseRequest`
This is the base request format that all Cohere text-family models use These models support top_p, top_k, max_tokens and temperature. 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(text)
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CohereCommandTextV14Request`
Cohere Command Text V14 supports top_p, top_k, temperature and max_tokens all functionality is implemented in CohereCommandBaseRequest 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(text)
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CohereCommandLightTextV14Request`
Cohere Command Light Text V14 supports top_p, top_k, temperature and max_tokens all functionality is implemented in CohereCommandBaseRequest 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(text)
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CohereCommandTextBaseResponse`
this is the base response format used by all text-family cohere models 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → str
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CohereCommandTextV14Response`
This is the response format for Cohere Command Text v14 It is implemented in CohereCommandTextBaseResponse 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → str
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CohereCommandLightTextV14Response`
This is the response format for Cohere Command Light Text v14 It is implemented in CohereCommandTextBaseResponse 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → str
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L79"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CohereEmbedBaseRequest`
All cohere command models use the same request format. Models support input text only. 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L104"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```

Cohere Embed V3 does not support top_k :param top_k: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```

Cohere Embed V3 does not support max_tokens :param max_tokens: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L96"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```

Cohere Embed V3 does not support top_p :param top_p: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L112"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```

Cohere Embed V3 does not support temperature :param temp: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(texts: list)
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L129"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CohereEmbedEnglishV3Request`
Request for Cohere Embed English V3. It supports top_p, top_k, temperature and max_tokens it is implemented in CohereEmbedBaseRequest 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L104"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```

Cohere Embed V3 does not support top_k :param top_k: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```

Cohere Embed V3 does not support max_tokens :param max_tokens: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L96"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```

Cohere Embed V3 does not support top_p :param top_p: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L112"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```

Cohere Embed V3 does not support temperature :param temp: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(texts: list)
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L137"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CohereEmbedMultilingualV3Request`
Request for Cohere Embed Multilingual V3. It supports top_p, top_k, temperature and max_tokens it is implemented in CohereEmbedBaseRequest 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L104"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```

Cohere Embed V3 does not support top_k :param top_k: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```

Cohere Embed V3 does not support max_tokens :param max_tokens: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L96"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```

Cohere Embed V3 does not support top_p :param top_p: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L112"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```

Cohere Embed V3 does not support temperature :param temp: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(texts: list)
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L145"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CohereEmbedBaseResponse`
All Cohere Embed models use the same response format. 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → List[float]
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L154"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CohereEmbedEnglishV3Response`
Response format for Cohere Embed English V3 It is implemented in CohereEmbedBaseResponse 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → List[float]
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L161"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CohereEmbedMultilingualV3Response`
Response for Cohere Embed Multilingual V3. it is implemented in CohereEmbedBaseResponse 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\cohere.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → List[float]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
