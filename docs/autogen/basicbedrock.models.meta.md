<!-- markdownlint-disable -->

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/meta.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `basicbedrock.models.meta`
File containing all of the definitions and implementations for the Meta family of requests and responses. Amazon docs currently do not have request schemas for Llama 2 13b and Llama 2 70b, only the chat versions 



---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/meta.py#L10"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MetaLlamaV2V3BaseRequest`
Meta LLama 2 13b chat request format. This model supports max_token, temperature and top_p. It does not support top_k 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/meta.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```

This model does not support top_k :param top_k: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/meta.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```

set the maximum tokens parameter. :param max_tokens: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/meta.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```

Set the top_p parameter. :param top_p: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/meta.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_prompt`

```python
set_prompt(text)
```

Update the prompt based on the input text. inserts text according to expected request conventions. :param text: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/meta.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_prompt_raw`

```python
set_prompt_raw(text)
```

Update the prompt based on the input text without regards to expected input format what you insert, is inserted raw without formatting :param text: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/meta.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_stop_words`

```python
set_stop_words(stop_words: List[str])
```

Meta Llama 2 models dont support stop words :param stop_words: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/meta.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```

set the temperature parameter. :param temp: :return: 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/meta.py#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MetaLlamaV2V3BaseResponse`
Response format of Meta Llama 2 V1 family chat response. 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/meta.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → str
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
