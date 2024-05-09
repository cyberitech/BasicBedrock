import boto3
from random import choice
from basicbedrock.guardrails import Guardrails
from basicbedrock import BasicBedrock


def test_content_policy():
    gr = Guardrails()
    gr.add_content_filter("SEXUAL","HIGH","HIGH")
    gr.install_guardrails()
    bb = BasicBedrock()
    model = choice([model for model in bb.get_available_models() if "embed" not in model])
    r = bb.invoke(model,"write a lewd story",guardrail=gr)
    print(r.get_answer())
    gr.uninstall_guardrails()


def test_filter_policy():
    gr = Guardrails()
    gr.add_topic_filter(definition="Conversation related to politics", examples=[
        "Jane Doe is a great president!",
        "Randy Randolph is the better presidential candidate ",
        "the House of Lords and the House of Commons ",
        "This election season will be a great match up between political parties"
    ])
    gr.install_guardrails()
    bb = BasicBedrock()
    model = choice([model for model in bb.get_available_models() if "embed" not in model])
    r = bb.invoke(model, "I am going to vote for in this year's elections", guardrail=gr)
    print(r.get_answer())
    gr.uninstall_guardrails()


def test_no_guardrail():
    bb = BasicBedrock()
    model = choice([model for model in bb.get_available_models() if "embed" not in model])
    r = bb.invoke(model, "simple test", guardrail=None)
    print(r.get_answer())


if __name__ == "__main__":
    test_no_guardrail()
    test_content_policy()
    test_filter_policy()