<!-- markdownlint-disable -->

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `basicbedrock.models.ai21`
File containing all of the definitions and implementations for the AI21 (jurassic) family of requests and responses. 



---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AI21Jurassic2BaseRequest`
AI21 Jurassic 2 request format. This model supports max_token, temperature and top_p, stop_sequences, count_penalty, presence_penalty and frequncy_penalty it does not support top_k as of right now there is no BasicBedrock support for penalty parameters 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```

This model does not support top_k :param top_k: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```

set the maximum tokens parameter. :param max_tokens: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```

Set the top_p parameter. :param top_p: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_prompt`

```python
set_prompt(text)
```

Update the prompt based on the input text. inserts text according to expected request conventions. :param text: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_prompt_raw`

```python
set_prompt_raw(text)
```

Update the prompt based on the input text without regards to expected input format what you insert, is inserted raw without formatting :param text: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_stop_words`

```python
set_stop_words(stop_words: List[str])
```

AI21 Jurassic 2 stop words allow either an empty list, or a single item of any string If more than a single stop word is provided, only the first element in the list will be used :param stop_words: a list of any stop words :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```

set the temperature parameter. :param temp: :return: 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L89"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AI21Jurassic2UltraV1Request`
Request format for  AI21 Jurassic 2 Ultra request. this model supports max_token, temperature and top_p. It does not support top_k This class is implemented in AI21Jurassic2BaseRequest. 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```

This model does not support top_k :param top_k: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```

set the maximum tokens parameter. :param max_tokens: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```

Set the top_p parameter. :param top_p: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_prompt`

```python
set_prompt(text)
```

Update the prompt based on the input text. inserts text according to expected request conventions. :param text: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_prompt_raw`

```python
set_prompt_raw(text)
```

Update the prompt based on the input text without regards to expected input format what you insert, is inserted raw without formatting :param text: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_stop_words`

```python
set_stop_words(stop_words: List[str])
```

AI21 Jurassic 2 stop words allow either an empty list, or a single item of any string If more than a single stop word is provided, only the first element in the list will be used :param stop_words: a list of any stop words :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```

set the temperature parameter. :param temp: :return: 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AI21Jurassic2MidV1Request`
Request format for AI21 Jurassic 2 Mid request. this model supports max_token, temperature and top_p. It does not support top_k This class is implemented in MetaLlama2ChatV1BaseRequest. 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```

This model does not support top_k :param top_k: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```

set the maximum tokens parameter. :param max_tokens: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```

Set the top_p parameter. :param top_p: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_prompt`

```python
set_prompt(text)
```

Update the prompt based on the input text. inserts text according to expected request conventions. :param text: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_prompt_raw`

```python
set_prompt_raw(text)
```

Update the prompt based on the input text without regards to expected input format what you insert, is inserted raw without formatting :param text: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_stop_words`

```python
set_stop_words(stop_words: List[str])
```

AI21 Jurassic 2 stop words allow either an empty list, or a single item of any string If more than a single stop word is provided, only the first element in the list will be used :param stop_words: a list of any stop words :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```

set the temperature parameter. :param temp: :return: 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AI21Jurassic2BaseResponse`
All AI21 Jurassic 2 models use the same response format. 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L112"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → List[float]
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AI21Jurassic2UltraV1Response`
Response format for AI21 Jurassic 2 Ultra response. It is implemented in AI21Jurassic2BaseResponse 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L112"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → List[float]
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L123"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AI21Jurassic2MidV1Response`
Response format for AI21 Jurassic 2 Mid response. It is implemented in AI21Jurassic2BaseResponse 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/ai21.py#L112"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → List[float]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
