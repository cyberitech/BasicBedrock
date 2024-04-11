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
        schema_inst = bb.get_model_request_object(model)
        schema_inst.set_prompt(prompt)
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
        schema_inst = bb.get_model_request_object(model)
        schema_inst.set_prompt(prompt)
        j = schema_inst.json()
        d = json.loads(j)
        r = bb.invoke(model, d, show_request=verbose)
        if verbose:
            print(r.get_answer_raw())
        print(f"done testing {model} in invoke with valid dict")


def test_invoke_with_invalid_dict(bb, verbose=False):
    all_models = bb.get_available_models()
    d = {"status": "invalid"}
    for model in all_models:
        print(f"now testing {model} in invoke with invalid dict")
        try:
            r = bb.invoke(model, d, show_request=verbose)
        except ValueError:
            pass  # we expect this, it should fail in this case
        if verbose:
            print(f"could not call model {model} in invoke with dict {d} (Ok)")
        print(f"done testing {model} in invoke with dict")


def test_get_boto3_body(bb,sess:boto3.session.Session, verbose=False):
    client = sess.client("bedrock-runtime")
    prompt = "tell me about foobar"
    all_models = bb.get_available_models()
    for model_id in all_models:
        print(f"now testing {model_id} invoke boto3 invoke_model() directly using get_boto3_body")
        body = bb.get_boto3_body(model_id, prompt)
        full_request = {
            "modelId": model_id,
            "body": body
        }
        if verbose:
            print(f"boto3 request: {full_request}")
        r = client.invoke_model(**full_request)
        assert (r['ResponseMetadata']['HTTPStatusCode'] == 200)
        print(f"done testing {model_id} invoke boto3 invoke_model() directly using get_boto3_body")


def single_run(bb, verbose=False):
    prompt = "tell me about foobar"
    bb.invoke("ai21.j2-mid-v1", prompt)


def test_set_params(bb, verbose=True):
    params = bb.params
    params["max_tokens"] = 88
    params["top_p"] = 0.88
    params["top_k"] = 88
    params["temp"] = .88
    params["stop_words"] = ["User:", "foobar"]
    bb.set_params(params)
    prompt = "Hittem hard with dem params doe"
    for model in bb.get_available_models():
        r = bb.invoke(model, prompt, show_request=verbose)
        if verbose:
            print(r.get_answer_raw())


if __name__ == "__main__":
    verbose = True
    session = boto3.session.Session(profile_name='default')
    bb = BasicBedrock(session=session)
    single_run(bb, verbose)
    test_invoke_with_string(bb, verbose=verbose)
    test_get_boto3_body(bb, sess=session, verbose=verbose)
    test_set_params(bb, verbose=verbose)
    test_invoke_with_invalid_json_blob(bb, verbose=verbose)
    test_invoke_with_valid_json_blob(bb, verbose=verbose)
    test_invoke_with_valid_dict(bb, verbose=verbose)
    test_invoke_with_invalid_dict(bb, verbose=verbose)
    print("All tests successful")
