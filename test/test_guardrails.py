import boto3
from basicbedrock.guardrails.baseclasses import *

def main():
    session = boto3.session.Session()
    client = session.client('bedrock')

    topic = Topic(
        name="foo",
        definition="bar",
        examples=["American Politics"]
    )
    topic_policy = TopicPolicyConfig(
        topicsConfig=[topic]
    )

    policy1 = PolicyConfig(
        name="a",
        description="b",
        blockedInputMessaging="stopped on input",
        blockedOutputsMessaging="stopped on output",
        topicPolicyConfig=topic_policy
    ).dict()

    filter = Filter(
        type="SEXUAL",
        inputStrength="LOW",
        outputStrength="MEDIUM",
    )
    content_policy = ContentPolicyConfig(
        filtersConfig=[filter]
    )

    policy2 = PolicyConfig(
        name="b",
        description="c",
        blockedInputMessaging="stopped on input",
        blockedOutputsMessaging="stopped on output",
        contentPolicyConfig=content_policy
    ).dict()

    for policy in (policy1, policy2):
        print(f"Creating: {policy}")
        r = client.create_guardrail(**policy)
        gid = r['guardrailId']
        client.delete_guardrail(guardrailIdentifier=gid)

if __name__ == "__main__":
    main()