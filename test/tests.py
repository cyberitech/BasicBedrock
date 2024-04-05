import sys
import os
import json
import boto3

sys.path.append(os.path.abspath('../src/basicbedrock'))
from basicbedrock import BasicBedrock


def test_invoke_with_string(bb, verbose=False):
    prompt = "tell me about foobar"
    all_models = bb.get_available_models()
    for model in all_models:
        print(f"now testing {model} in invoke with string")
        r = bb.invoke(model, prompt, show_request=verbose)
        if verbose:
            print(r.get_answer_raw())
        print(f"done testing {model} in invoke with string")

def test_invoke_with_invalid_json_blob(bb, verbose=False):
    prompt = "{\"status\":\"invalid\"}"
    all_models = bb.get_available_models()
    for model in all_models:
        print(f"now testing {model} in invoke with invalid json blob")
        r = bb.invoke(model, prompt, show_request=verbose)
        if verbose:
            print(r.get_answer_raw())
        print(f"done testing {model} in invoke with invalid json blob")

def test_invoke_with_valid_json_blob(bb, verbose=False):
    prompt = "tell me about foobar"
    all_models = bb.get_available_models()
    for model in all_models:
        print(f"now testing {model} in invoke with valid json blob")
        schema_inst = bb.get_model_schema_object(model)
        schema_inst.update_prompt(prompt)
        blob = schema_inst.json()
        r = bb.invoke(model, blob, show_request=verbose)
        if verbose:
            print(r.get_answer_raw())
        print(f"done testing {model} in invoke with valid json blob")

def test_invoke_with_valid_dict(bb, verbose=False):
    prompt = "tell me about foobar"
    all_models = bb.get_available_models()
    for model in all_models:
        print(f"now testing {model} in invoke with valid dict")
        schema_inst = bb.get_model_schema_object(model)
        schema_inst.update_prompt(prompt)
        j = schema_inst.json()
        d = json.loads(j)
        r = bb.invoke(model, d, show_request=verbose)
        if verbose:
            print(r.get_answer_raw())
        print(f"done testing {model} in invoke with valid dict")

def test_invoke_with_invalid_dict(bb, verbose=False):
    all_models = bb.get_available_models()
    d = {"status":"invalid"}
    for model in all_models:
        print(f"now testing {model} in invoke with invalid dict")
        try:
            r = bb.invoke(model, d, show_request=verbose)
        except ValueError:
            pass # we expect this, it should fail in this case
        if verbose:
            print(f"could not call model {model} in invoke with dict {d} (Ok)")
        print(f"done testing {model} in invoke with dict")

def single_run(bb, verbose=False):
    prompt = "tell me about foobar"
    bb.invoke("cohere.command-text-v14",prompt)

if __name__ == "__main__":
    verbose = True
    session = boto3.session.Session(profile_name='default')
    bb = BasicBedrock(session=session)
    single_run(bb, verbose)

    test_invoke_with_string(bb, verbose=verbose)
    test_invoke_with_invalid_json_blob(bb, verbose=verbose)
    test_invoke_with_valid_json_blob(bb, verbose=verbose)
    test_invoke_with_valid_dict(bb, verbose=verbose)
    test_invoke_with_invalid_dict(bb, verbose=verbose)
    print("All tests successful")