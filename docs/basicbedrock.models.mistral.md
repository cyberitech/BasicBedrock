<!-- markdownlint-disable -->

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `basicbedrock.models.mistral`






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L6"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MistralBaseRequest`
Base request for Mistral family of models. this mnodel supports temperature, top_p, top_k and max_tokens 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(text)
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MistralMistral7bInstructV0_2Request`
Request format for Mistral 7b Instruct V0:2 This model supports temperature, top_p, top_k and max_tokens This class is implemented in MistralBaseRequest 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(text)
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MistralMistral8x7bInstructV0_1Request`
Request format for Mistral 8x7b Instruct V0:1 This model supports temperature, top_p, top_k and max_tokens This class is implemented in MistralBaseRequest 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(text)
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MistralMistralLarge2402V1_0Request`
Request format for Mistral Large 2402 V1:0 This model supports temperature, top_p, top_k and max_tokens This class is implemented in MistralBaseRequest 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt`

```python
update_prompt(text)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_prompt_raw`

```python
update_prompt_raw(text)
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MistralBaseResponse`
Base response format for Mistral Instruct family of models. 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → str
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L71"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MistralMistral7bInstructV0_2Response`
Response format for Mistral 7b Instruct V0:2 This class is implemented in MistralBaseResponse 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → str
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L78"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MistralMistral8x7bInstructV0_1Response`
Response format for Mistral 8x7b Instruct V0:2 This class is implemented in MistralBaseResponse 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → str
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L85"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MistralMistralLarge2402V1_0Response`
Response format for Mistral Large 2402 v1:0 This class is implemented in MistralInstructBaseResponse 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main\src\basicbedrock\models\mistral.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer() → str
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
