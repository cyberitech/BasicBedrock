# BasicBedrock
AWS Bedrock provides a variety of foundational models to AWS customers.  Each model family requires their own request structure, yet the underlying semantics are roughly common; there is always a field for the textual input prompt, and often there are fields to define maximum desired output, stop words, P, K and Temperature values.

This package aims to abstract away all of that. 

For model requests, top_p, top_k, temp, max_tokens, stop_words and prompts are all abstracted away.  For model responses, the answer itself is extracted, but the caller can also get the raw dict object passed back by boto3 if they wish.

## Design Principles
I designed this around the following design principles:
 * If a paramater is specified, it will be used whenever possible.  If not possible, it is (silently) ignored.
 * If a parameter is not specified, but it is required, a default parameter will be used (see below)
 * If a parameter is required to be in a certain format (such as a prompt) this is done by default
 * If multiple parameters are specified (stop_words), but only 0 or 1 are valid, then the first valid one will be used. If none are valid, then the default will be used

### Default Parameters
There is no default prompt.  The user must always provide their prompt for every call to invoke().  Unless the caller specifies otherwise, the following defaults are used:
```python
top_p: float = 0.5
top_k: int = 125
temp: float = 0.5
max_tokens: int = 250
stop_words: List[str] = []
```


## Usage
### Installation
```bash
pip install basicbedrock
```

### Example
Rather simple to use.  See [examples](./examples) for some usage examples.

```python
import boto3
from basicbedrock import BasicBedrock

session = boto3.session.Session(profile_name="default",region_name="us-west-2")
bb = BasicBedrock(session=session)
model = "anthropic.claude-3-sonnet-20240229-v1:0"
prompt = "Tell me about flowers"
r = bb.invoke(model, prompt)
print(r.get_answer())
```

