<!-- markdownlint-disable -->

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `basicbedrock.guardrails_baseclasses`
Contains all of the base classes for working with guardrails 

reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_guardrail.html 



**Example:**
 ```
     session = boto3.session.Session()
     client = session.client('bedrock')

     filter = Filter(
         type="SEXUAL",
         inputStrength="LOW",
         outputStrength="MEDIUM",
     )
     content_policy = ContentPolicyConfig(
         filtersConfig=[filter]
     )

     policy = PolicyConfig(
         name="b",
         description="c",
         blockedInputMessaging="stopped on input",
         blockedOutputsMessaging="stopped on output",
         contentPolicyConfig=content_policy
     ).dict()

     print(f"Creating: {policy}")
     r = client.create_guardrail(**policy)
     gid = r['guardrailId']
     client.delete_guardrail(guardrailIdentifier=gid)
``` 



---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BotoizerBaseModel`




<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(*args, **kwargs)
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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `dict`

```python
dict(*args, **kwargs) → dict
```

override default dict behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.dict() :param kwargs: kwargs passed onto BaseModel.dict() :return: model dict suitable for boto3 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `json`

```python
json(*args, **kwargs) → str
```

override default json behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.json() :param kwargs: kwargs passed onto BaseModel.json() :return: model json suitable for boto3 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L71"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `FilterType`
An enumeration. 

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L79"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(*args, **kwargs)
```

SEXUAL = 'SEXUAL' 

VIOLENCE = 'VIOLENCE' 

HATE = 'HATE' 

INSULTS = 'INSULTS' 

MISCONDUCT = 'MISCONDUCT' 

PROMPT_ATTACK = 'PROMPT_ATTACK' 





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `FilterStrength`
An enumeration. 

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L97"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(*args, **kwargs)
```

LOW = 'LOW' 

MEDIUM = 'MEDIUM' 

HIGH = 'HIGH' 

NONE = 'NONE' 





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Topic`




<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L113"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(*args, **kwargs)
```

name: str 

definition: str 

examples: List[str] 

type: str = "DENY" 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `dict`

```python
dict(*args, **kwargs) → dict
```

override default dict behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.dict() :param kwargs: kwargs passed onto BaseModel.dict() :return: model dict suitable for boto3 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `json`

```python
json(*args, **kwargs) → str
```

override default json behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.json() :param kwargs: kwargs passed onto BaseModel.json() :return: model json suitable for boto3 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L123"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TopicPolicyConfig`




<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(*args, **kwargs)
```

topicsConfig: List[Topic] 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `dict`

```python
dict(*args, **kwargs) → dict
```

override default dict behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.dict() :param kwargs: kwargs passed onto BaseModel.dict() :return: model dict suitable for boto3 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `json`

```python
json(*args, **kwargs) → str
```

override default json behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.json() :param kwargs: kwargs passed onto BaseModel.json() :return: model json suitable for boto3 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Filter`




<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L138"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(*args, **kwargs)
```

type: FilterType 

inputStrength: FilterStrength 

outputStrength: FilterStrength 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `dict`

```python
dict(*args, **kwargs) → dict
```

override default dict behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.dict() :param kwargs: kwargs passed onto BaseModel.dict() :return: model dict suitable for boto3 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `json`

```python
json(*args, **kwargs) → str
```

override default json behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.json() :param kwargs: kwargs passed onto BaseModel.json() :return: model json suitable for boto3 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L147"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ContentPolicyConfig`




<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(*args, **kwargs)
```

filtersConfig: List[Filter] 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `dict`

```python
dict(*args, **kwargs) → dict
```

override default dict behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.dict() :param kwargs: kwargs passed onto BaseModel.dict() :return: model dict suitable for boto3 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `json`

```python
json(*args, **kwargs) → str
```

override default json behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.json() :param kwargs: kwargs passed onto BaseModel.json() :return: model json suitable for boto3 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L157"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `WordConfig`




<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(*args, **kwargs)
```

text: str 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `dict`

```python
dict(*args, **kwargs) → dict
```

override default dict behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.dict() :param kwargs: kwargs passed onto BaseModel.dict() :return: model dict suitable for boto3 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `json`

```python
json(*args, **kwargs) → str
```

override default json behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.json() :param kwargs: kwargs passed onto BaseModel.json() :return: model json suitable for boto3 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L167"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ManagedWordListConfig`




<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L170"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(*args, **kwargs)
```

text: str 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `dict`

```python
dict(*args, **kwargs) → dict
```

override default dict behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.dict() :param kwargs: kwargs passed onto BaseModel.dict() :return: model dict suitable for boto3 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `json`

```python
json(*args, **kwargs) → str
```

override default json behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.json() :param kwargs: kwargs passed onto BaseModel.json() :return: model json suitable for boto3 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L177"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `WordPolicyConfig`




<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L181"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(*args, **kwargs)
```

wordsConfig: List[WordConfig] 

managedWordListsConfig: List[ManagedWordListConfig] 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `dict`

```python
dict(*args, **kwargs) → dict
```

override default dict behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.dict() :param kwargs: kwargs passed onto BaseModel.dict() :return: model dict suitable for boto3 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `json`

```python
json(*args, **kwargs) → str
```

override default json behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.json() :param kwargs: kwargs passed onto BaseModel.json() :return: model json suitable for boto3 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L189"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `PiiEntityConfig`




<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L193"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(*args, **kwargs)
```

type: str 

action: str 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `dict`

```python
dict(*args, **kwargs) → dict
```

override default dict behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.dict() :param kwargs: kwargs passed onto BaseModel.dict() :return: model dict suitable for boto3 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `json`

```python
json(*args, **kwargs) → str
```

override default json behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.json() :param kwargs: kwargs passed onto BaseModel.json() :return: model json suitable for boto3 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L201"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RegexConfig`




<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L207"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(*args, **kwargs)
```

name: str 

description: str 

pattern: str 

action: str 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `dict`

```python
dict(*args, **kwargs) → dict
```

override default dict behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.dict() :param kwargs: kwargs passed onto BaseModel.dict() :return: model dict suitable for boto3 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `json`

```python
json(*args, **kwargs) → str
```

override default json behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.json() :param kwargs: kwargs passed onto BaseModel.json() :return: model json suitable for boto3 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L217"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SensitiveInformationPolicyConfig`




<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L221"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(*args, **kwargs)
```

piiEntitiesConfig: List[PiiEntityConfig] 

regexesConfig: List[RegexConfig] 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `dict`

```python
dict(*args, **kwargs) → dict
```

override default dict behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.dict() :param kwargs: kwargs passed onto BaseModel.dict() :return: model dict suitable for boto3 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `json`

```python
json(*args, **kwargs) → str
```

override default json behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.json() :param kwargs: kwargs passed onto BaseModel.json() :return: model json suitable for boto3 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L229"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Tag`




<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L233"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(*args, **kwargs)
```

key: str 

value: str 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `dict`

```python
dict(*args, **kwargs) → dict
```

override default dict behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.dict() :param kwargs: kwargs passed onto BaseModel.dict() :return: model dict suitable for boto3 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `json`

```python
json(*args, **kwargs) → str
```

override default json behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.json() :param kwargs: kwargs passed onto BaseModel.json() :return: model json suitable for boto3 


---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L241"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `PolicyConfig`




<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L261"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(*args, **kwargs)
```

name: str 

description: str 

topicPolicyConfig: Optional[TopicPolicyConfig] = None 

contentPolicyConfig: Optional[ContentPolicyConfig] = None 

wordPolicyConfig: Optional[WordPolicyConfig] = None 

sensitiveInformationPolicyConfig: Optional[SensitiveInformationPolicyConfig] = None 

blockedInputMessaging: str = None 

blockedOutputsMessaging: str = None 

kmsKeyId: Optional[str] = None 

tags: Optional[List[Tag]] = None 

clientRequestToken: Optional[str] = None 


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

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `dict`

```python
dict(*args, **kwargs) → dict
```

override default dict behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.dict() :param kwargs: kwargs passed onto BaseModel.dict() :return: model dict suitable for boto3 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `json`

```python
json(*args, **kwargs) → str
```

override default json behavior.  boto3 does not want None or null values, we need to exclude them from building This function overrides so that the default behaviour is to exclude_none=True :param args: args passed onto BaseModel.json() :param kwargs: kwargs passed onto BaseModel.json() :return: model json suitable for boto3 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails_baseclasses.py#L254"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `minimim_policy_validator`

```python
minimim_policy_validator() → Self
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
