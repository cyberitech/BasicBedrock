import sys
import os
import boto3
import random
from basicbedrock import BasicBedrock

# create a session (optional, but nice)
session = boto3.session.Session(profile_name='default')
client = BasicBedrock(session=session)

print("Available models:")
client.print_available_models()
print("\n")

available_models = client.get_available_models()
some_model = random.choice(available_models)
print(f"randomly chose model {some_model}")
print(f"what a model request looks like for {some_model}")
client.print_model_schema(some_model, indent=4)
print("\n")

prompt = "tell me about kittens"
if "embed" in some_model:
    print(f"This model does embeddings.  Lets see the embedding for \"{prompt}\"")
else:
    print(f"lets ask the model: \"{prompt}\"")

# run inference
response_obj = client.invoke(some_model, prompt, show_request=True)
response_text = response_obj.get_answer()
print(response_text)