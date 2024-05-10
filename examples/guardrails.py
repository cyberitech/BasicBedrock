from random import choice
from basicbedrock import BasicBedrock, Guardrails

gr = Guardrails()
bb = BasicBedrock()

# add a content filter
gr.add_content_filter("SEXUAL","HIGH","HIGH")

# add a topic filter
gr.add_topic_filter(definition="Conversation related to politics", examples=[
    "Jane Doe is a great president!",
    "Randy Randolph is the better presidential candidate ",
    "the House of Lords and the House of Commons ",
    "This election season will be a great match up between political parties"
])

# apply the guardrails to the account
gr.install_guardrails()

# choose random model
model = choice([model for model in bb.get_available_models() if "embed" not in model])

# test the topic filter
r = bb.invoke(model, "I am going to vote for in this year's elections", guardrail=gr)
print(r.get_answer())

# test the content filter
r = bb.invoke(model, "I am going to vote for in this year's elections", guardrail=gr)
print(r.get_answer())

# remove the guardrails from the aws account (optional)
gr.uninstall_guardrails()
