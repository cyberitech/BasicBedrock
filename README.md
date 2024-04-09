# BasicBedrock
AWS Bedrock provides a variety of foundational models to AWS customers.  Each model family requires their own request structure, yet the underlying semantics are roughly common; there is always a field for the textual input prompt, and often there are fields to define maximum desired output, stop words, P, K and Temperature values.

This package aims to abstract away all of that.  Currently, it only abstracts parameters P, K, temperature, max_tokens, the input prompt and the answer text, but I plan to also inlcude abstraction layers for the other output metedata fields as well.

## Installation
```bash
pip install basicbedrock
```

## Usage
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

