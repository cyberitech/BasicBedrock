"""
This file shows how to play with setting params
"""
import sys
import os
import random
import boto3

try:
    from basicbedrock import BasicBedrock
except:  # we are not installed, only working in project directory, include src directory
    sys.path.append(os.path.abspath('../src/basicbedrock'))
    from basicbedrock import BasicBedrock

prompt="tell me about prague"
session = boto3.session.Session(profile_name='default')
bb = BasicBedrock(session=session)
some_model = random.choice(bb.get_available_models())

# Examine default params
default_params = bb.params
print(f"default params: {default_params}")
print("invoke default params")
r = bb.invoke(some_model, prompt, show_request=True)
print(r.get_answer())

# Change the current invocation params
new_params = default_params.copy()
new_params["top_k"] = 88
new_params["top_p"] = 0.88
new_params["max_tokens"] = 888
new_params["temp"] = 0.88

# apply the new params
bb.set_params(new_params)
# or, equivalently
bb.params = new_params

print(f"new params: {new_params}")
print("invoke new params")
r = bb.invoke(some_model, prompt, show_request=True)
print(r.get_answer())
