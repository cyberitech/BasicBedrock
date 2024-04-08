import boto3
from basicbedrock import BasicBedrock

session = boto3.session.Session(profile_name="default",region_name="us-west-2")
bb = BasicBedrock(session=session)
model = "anthropic.claude-3-sonnet-20240229-v1:0"
prompt = "Tell me about flowers"
params = {
    "top_p": 0.88,
    "top_k": 88,
    "max_tokens": 88,
    "temp": 0.88
}
bb.set_params(params)
r = bb.invoke(model, prompt)
print(r.get_answer())