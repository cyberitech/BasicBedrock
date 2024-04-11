<!-- markdownlint-disable -->

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `basicbedrock.models.baseclasses`
File containing the base classes used for all model requests and responses. Contains abstract base classes for the requests and responses, as well as a concrete class for hyperparameters p, k, temp and max_tokens 



---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Hyperparams`
Hyperparameters for a model. Values are top_p, top_k, temp and max_tokens Not all models support all parameters. Any parameters used in here which are not supported by the model are ignored at runtime 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BaseAbstractRequest`
Abstract base class for all model requests. All model requests must inherit this class. update_prompt and update_promp_raw differ in the fact that some models expect a certain request format to work properly, eg, in certain cases boto3 may reject the request if the prompt does not begin with "Human:"    update_prompt will format all prompts as expected by the model, whereas update_prompt_raw will input text without formatting. The other abstract methods all deal with setting hyperparam values P, K, temp, and max tokens. Additionally, two non abstract methods allow the caller to return the request as a dict or json. 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_dict`

```python
get_dict()
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L69"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_json`

```python
get_json(indent: int = None)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L101"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_k`

```python
set_k(top_k: int)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L109"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_max_tokens`

```python
set_max_tokens(max_tokens: int)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L97"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_p`

```python
set_p(top_p: float)
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_params`

```python
set_params(params: dict)
```

Sets the hyperparameters of the request (p, k, temp, max_tokens) :param params: :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_prompt`

```python
set_prompt(text: str)
```

Updates the prompt while maintaining its expected internal prompt structure Example, if the prompt must begin with 'Human:' this will be maintained :param text: the prompt you want to use :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_prompt_raw`

```python
set_prompt_raw(text: str)
```

Updates the prompt without regards to any expected prompt structure. this is used for very precisely modifying prompts. :param text: the exact prompt you want to use :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_stop_words`

```python
set_stop_words(stop_words: List[str])
```

Sets the stop words used in the model. If the model does not support stop words, this is ignored :param stop_words: the list of strings :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L105"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_temp`

```python
set_temp(temp: float)
```






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L114"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BaseAbstractResponse`
This is the abstract base model for all model responses. It will internally store the exact result provided by boto3 as a dict. methods are exposed to return to the caller the raw response as dict or json. The abstract method get_answer serves to parse out the actual response and return it, ignoring the associated metadata. 

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L123"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(res: dict)
```






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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L127"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer`

```python
get_answer()
```

Returns only the answer to the prompt.  May be a string or a list in the case of embeddings. 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L140"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer_json`

```python
get_answer_json() → str
```

returns the internal dict answer as a json string :return: json string 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/models/baseclasses.py#L134"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_answer_raw`

```python
get_answer_raw() → dict
```

Returns a copy of the dict object returned by the boto sdk 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
