<!-- markdownlint-disable -->

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `basicbedrock.models.meta`
File containing all of the definitions and implementations for the Meta family of requests and responses. Amazon docs currently do not have request schemas for Llama 2 13b and Llama 2 70b, only the chat versions 



---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MetaLlama2ChatV1BaseRequest`
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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```

This model does not support top_k :param top_k: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```

set the maximum tokens parameter. :param max_tokens: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```

Set the top_p parameter. :param top_p: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```

set the temperature parameter. :param temp: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```

Update the prompt based on the input text. inserts text according to expected request conventions. :param text: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(text)
```

Update the prompt based on the input text without regards to expected input format what you insert, is inserted raw without formatting :param text: :return: 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MetaLlama213bChatV1Request`
Request format for Meta Llama 2 13b chat. this model supports max_token, temperature and top_p. It does not support top_k This class is implemented in MetaLlama2ChatV1BaseRequest. 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```

This model does not support top_k :param top_k: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```

set the maximum tokens parameter. :param max_tokens: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```

Set the top_p parameter. :param top_p: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```

set the temperature parameter. :param temp: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```

Update the prompt based on the input text. inserts text according to expected request conventions. :param text: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(text)
```

Update the prompt based on the input text without regards to expected input format what you insert, is inserted raw without formatting :param text: :return: 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L81"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MetaLlama270bChatV1Request`
Request format for Meta Llama 2 70b chat. this model supports max_token, temperature and top_p. It does not support top_k This class is implemented in MetaLlama2ChatV1BaseRequest. 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```

This model does not support top_k :param top_k: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```

set the maximum tokens parameter. :param max_tokens: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```

Set the top_p parameter. :param top_p: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```

set the temperature parameter. :param temp: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```

Update the prompt based on the input text. inserts text according to expected request conventions. :param text: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(text)
```

Update the prompt based on the input text without regards to expected input format what you insert, is inserted raw without formatting :param text: :return: 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MetaLlama2V1BaseResponse`
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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → str
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L99"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MetaLlama213bChatV1Response`
Response format of Meta Llama 2 13b chat response. Implemented in MetaLlama2V1BaseResponse. 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → str
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L106"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MetaLlama270bChatV1Response`
Response format of Meta Llama 2 70b chat response. Implemented in MetaLlama2V1BaseResponse. 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\meta.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → str
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
