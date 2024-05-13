from random import choice
import json
import boto3

from basicbedrock import *


def test_content_policy(bb: BasicBedrock, verbose=False):
    gr = Guardrails()
    gr.add_content_filter("SEXUAL","HIGH","HIGH")
    gr.install_guardrails()
    model = choice([model for model in bb.get_available_models() if "embed" not in model])
    r = bb.invoke(model,"write a lewd story",guardrail=gr)
    if verbose: print(r.get_answer())
    gr.uninstall_guardrails()


def test_filter_policy(bb: BasicBedrock, verbose=False):
    gr = Guardrails()
    gr.add_topic_filter(definition="Conversation related to politics", examples=[
        "Jane Doe is a great president!",
        "Randy Randolph is the better presidential candidate ",
        "the House of Lords and the House of Commons ",
        "This election season will be a great match up between political parties"
    ])
    gr.install_guardrails()
    model = choice([model for model in bb.get_available_models() if "embed" not in model])
    r = bb.invoke(model, "I am going to vote for in this year's elections", guardrail=gr)
    if verbose: print(r.get_answer())
    gr.uninstall_guardrails()


def test_no_guardrail(bb: BasicBedrock, verbose=False):
    bb = BasicBedrock()
    model = choice([model for model in bb.get_available_models() if "embed" not in model])
    r = bb.invoke(model, "simple test", guardrail=None)
    if verbose: print(r.get_answer())


def test_invoke_with_string(bb:BasicBedrock, verbose=False):
    prompt = "tell me about foobar"
    all_models = bb.get_available_models()
    for model in all_models:
        print(f"now testing {model} in invoke with string")
        r = bb.invoke(model, prompt, show_request=verbose)
        if verbose:
            print(r.get_answer())
        print(f"done testing {model} in invoke with string")


def test_invoke_with_invalid_json_blob(bb:BasicBedrock, verbose=False):
    prompt = "{\"status\":\"invalid\"}"
    all_models = bb.get_available_models()
    for model in all_models:
        print(f"now testing {model} in invoke with invalid json blob")
        r = bb.invoke(model, prompt, show_request=verbose)
        if verbose:
            print(r.get_answer())
        print(f"done testing {model} in invoke with invalid json blob")


def test_invoke_with_valid_json_blob(bb:BasicBedrock, verbose=False):
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


def test_invoke_with_valid_dict(bb:BasicBedrock, verbose=False):
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


def test_invoke_with_invalid_dict(bb:BasicBedrock, verbose=False):
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


def test_get_boto3_body(bb:BasicBedrock,sess:boto3.session.Session, verbose=False):
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


def single_run(bb:BasicBedrock, verbose=False):
    prompt = "tell me about foobar"
    r=bb.invoke("cohere.command-r-v1:0", prompt)
    if verbose: print(r.get_answer())


def test_set_params(bb:BasicBedrock, verbose=True):
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


def test_context_window_limits(bb:BasicBedrock, verbose=False):
    for model_id,ctxt in model_request_context_windows.items():
        if not ctxt:  # embeds have no max
            continue
        print(f"now testing {model_id} test_context_window_limits")
        prompt = "My name is the real slim shady" * ctxt
        r = bb.invoke(model_id, prompt, show_request=verbose)


def test_max_tokens(bb:BasicBedrock, verbose=False):
    for model_id,max_token in model_request_max_outputs.items():
        if not max_token:  # embeds have no max
            continue
        print(f"now testing {model_id} test_max_tokens")
        params = {
            "max_tokens": max_token,
        }
        print(params)
        prompt = "this is a test"
        bb.params = params
        r = bb.invoke(model_id, prompt, show_request=verbose)


def test_get_prompts(bb:BasicBedrock, verbose=True):
    prompt = "test of the prompt retreival"
    for model in bb.get_available_models():
        req_obj = bb.get_model_request_object(model)
        req_obj.set_prompt(prompt)
        output = req_obj.get_prompt()
        if verbose:
            print(model)
            print(json.dumps(output))


if __name__ == "__main__":
    verbose = True
    session = boto3.session.Session(profile_name='default')
    bb = BasicBedrock(session=session)
    single_run(bb, verbose)
    test_get_prompts(bb,verbose)
    test_no_guardrail(bb, verbose)
    test_content_policy(bb, verbose)
    test_filter_policy(bb, verbose)
    test_invoke_with_string(bb, verbose=verbose)
    test_get_boto3_body(bb, sess=session, verbose=verbose)
    test_set_params(bb, verbose=verbose)
    test_invoke_with_invalid_json_blob(bb, verbose=verbose)
    test_invoke_with_valid_json_blob(bb, verbose=verbose)
    test_invoke_with_valid_dict(bb, verbose=verbose)
    test_invoke_with_invalid_dict(bb, verbose=verbose)
    test_context_window_limits(bb,verbose=verbose)
    test_max_tokens(bb,verbose=verbose)
    print("All tests successful")
