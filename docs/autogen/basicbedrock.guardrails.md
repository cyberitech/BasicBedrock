<!-- markdownlint-disable -->

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `basicbedrock.guardrails`






---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Guardrails`




<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails.py#L10"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(session: Session = None)
```

A GuardRails object represents an abstraction of Amazon Guardrails. 

This class currently supports both topic and content based filtering. 

Topical content filtering allows the developer to define a topic of conversation to block. 

Content filtering provides an enumeration of content to filter, such as hate or sexual. 

This class contains an internal representation of these configurations.  During instantiation, a uuid4 value will be generated and used to identify the guardrails rules in the AWS account. 

Once rules are configured by calling add_topic_filter() or add_content_filter(), you must call install_guardrails() to apply the rules to the account. 

As part of cleaning up when done, you should call uninstall_guardrails() when you are done using this object, although if you do not, you can use the guardrail in the future for other things. 

:param session: 




---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails.py#L70"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_content_filter`

```python
add_content_filter(
    content_type: Union[FilterType, str],
    input_strength: Union[FilterStrength, str] = 'HIGH',
    output_strength: Union[FilterStrength, str] = 'HIGH'
)
```

Add a content filter to this guardrails instance.  

A content filter contains an enumeration of content types, such as HATE, INSULT, PROMPT_ATTACK and others, combined with a strenght of the filtering, such as LOW MEDIUM or HIGH.  

An enumeration of the content filter is found in basicbedrock.guardrails.baseclasses.FilterType  

An enumeration of the filter strengths are found into basicbedrock.guardrails.baseclasses.FilterStrength  

:param content_type: a content type found in basicbedrock.guardrails.baseclasses.FilterType :param input_strength: a filter strenght found in basicbedrock.guardrails.baseclasses.FilterStrength :param output_strength: a filter strenght found in basicbedrock.guardrails.baseclasses.FilterStrength :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_topic_filter`

```python
add_topic_filter(definition: str, examples: List[str])
```

Add a topic filter to this Guardrails instance.  

This requires a definition of a topic, and examples of this topic of conversation. 

Example definition: "Investment advice refers to inquires, guidance or recommendations regarding the management or allocation of funds or assets with the goal of generating returns or achieving specific financial objectives." 

Example example: ["You should invest all your money in doge coin"] 

:param definition: a string of 200 characters or less defining the topic to be blocked :param examples: a list of examples of less than 100 characters each highlighting blocked content to include for the topic filter :return: None 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails.py#L153"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `clear_content_guardrails_config`

```python
clear_content_guardrails_config()
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails.py#L138"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `clear_guardrails_config`

```python
clear_guardrails_config()
```

Clears the existing guardrails configuration of this instance. 

It does not, however remove the guardrails from your AWS account if it has already been installed. 

To remove an this guardrails after it has been installed to your account, you should call uninstall_guardrails() :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `clear_topical_guardrails_config`

```python
clear_topical_guardrails_config()
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails.py#L168"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_content_guardrails_config`

```python
get_content_guardrails_config()
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails.py#L156"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_guardrails_config`

```python
get_guardrails_config() → dict
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails.py#L162"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_topical_guardrails_config`

```python
get_topical_guardrails_config()
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails.py#L174"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `install_guardrails`

```python
install_guardrails()
```

Installs into your account a guardrail definition equivalent to how this Guardrails instance is configured.  

This can be called multiple times to update the Guardrails definition with new information. :return: 

---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails.py#L171"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `print_content_guardrails_config`

```python
print_content_guardrails_config()
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails.py#L159"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `print_guardrails_config`

```python
print_guardrails_config()
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails.py#L165"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `print_topical_guardrails_config`

```python
print_topical_guardrails_config()
```





---

<a href="https://github.com/cyberitech/BasicBedrock/tree/main/src/basicbedrock/guardrails.py#L193"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `uninstall_guardrails`

```python
uninstall_guardrails()
```

Deletes from your AWS account the guardrail ID referenced by this Guardrails instance :return:  None 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
