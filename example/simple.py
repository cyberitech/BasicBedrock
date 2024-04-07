import boto3
from basicbedrock import BasicBedrock

session = boto3.session.Session(profile_name="default",region_name="us-west-2")
bb = BasicBedrock(session=session)
model = "anthropic.claude-3-sonnet-20240229-v1:0"
prompt = "Tell me about flowers"
r = bb.invoke(model, prompt)
print(r.get_answer())