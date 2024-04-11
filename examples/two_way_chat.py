"""
This file is an example demonstrating how to create a two-way chat between two arbitrary models
Really its just for toy purposes to exemplify creative ways to use this library
"""
import boto3
from random import choice
from basicbedrock import BasicBedrock

# create a session using my default awscli profile using region us-west-2
session = boto3.session.Session(profile_name="default", region_name="us-west-2")
bb = BasicBedrock(session)

# just some reasonable parameters.
# we are going to limit the models to a 50,000 token chat history
# but, we will rig up our own sliding window of sorts to keep the conversation going ad infinitum
SLIDING_WINDOW_SIZE = 50000
params = {
    "top_p": 0.5,
    "top_k": 150,
    "temp": 0.5,
    "max_tokens": SLIDING_WINDOW_SIZE
}


# helper function to implement a sliding attention window
def sliding_window(conversation: str) -> str:
    # truncate the conversation window to make it a sliding window
    if len(conversation) > SLIDING_WINDOW_SIZE:
        conversation = conversation[-1 * SLIDING_WINDOW_SIZE:]
    return conversation


# we do not want any models meant for creating embeddings
chat_models = [model for model in bb.get_available_models() if "embed" not in model]

# chose two arbitrary models
model_a = choice(chat_models)
model_b = choice(chat_models)

print(f"{model_a} will chat with {model_b}")

# let us kick it off with a story-telling scenario
initial_prompt = f"Hello! My name is {model_a}, tell me a story, and you and I will have a conversation!"

# initialize the conversation window
chat_history = initial_prompt

print(f"[+] {model_a}: {initial_prompt}")

while True:
    # truncate the conversation window to make it a sliding window
    chat_history = sliding_window(chat_history)
    # pass the conversation to model b
    model_b_answer = bb.invoke(model_b, chat_history).get_answer()
    print(f"[+] {model_b}: {model_b_answer}")
    # append model b answer to the chat history
    chat_history += "\n\n" + model_b_answer
    # again, truncate to window size if needed
    chat_history = sliding_window(chat_history)
    # pass the conversation to model a
    model_a_answer = bb.invoke(model_a, chat_history).get_answer()
    print(f"[+] {model_a}: {model_a_answer}")
    # once again, append model a answer to the chat history
    chat_history += "\n\n" + model_b_answer
