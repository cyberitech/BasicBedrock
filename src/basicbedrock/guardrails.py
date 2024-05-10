from typing import Union
from uuid import uuid4
import json
import boto3
from basicbedrock.guardrails_baseclasses import *


class Guardrails:

    def __init__(self, session: boto3.session.Session = None):
        """
        A GuardRails object represents an abstraction of Amazon Guardrails.\n
        This class currently supports both topic and content based filtering.\n
        Topical content filtering allows the developer to define a topic of conversation to block.\n
        Content filtering provides an enumeration of content to filter, such as hate or sexual.\n
        This class contains an internal representation of these configurations.  During instantiation, a uuid4 value
        will be generated and used to identify the guardrails rules in the AWS account.\n
        Once rules are configured by calling add_topic_filter() or add_content_filter(), you must call
        install_guardrails() to apply the rules to the account.\n
        As part of cleaning up when done, you should call uninstall_guardrails() when you are done using this object,
        although if you do not, you can use the guardrail in the future for other things.

        :param session:
        """
        if not session:
            session = boto3.session.Session()
        self.client = session.client('bedrock')
        self.topic_configuration: Optional[TopicPolicyConfig] = None
        self.content_configuration: Optional[ContentPolicyConfig] = None
        self.guardrail_policy: Optional[PolicyConfig] = None
        self.guardrail_version: Optional[int] = None
        self.guardrail_id: Optional[str] = None
        self.uuid = str(uuid4())

    def add_topic_filter(self, definition:str, examples: List[str]):
        """
        Add a topic filter to this Guardrails instance. \n
        This requires a definition of a topic, and examples of this topic of conversation.\n
        Example definition: "Investment advice refers to inquires, guidance or recommendations regarding the management
        or allocation of funds or assets with the goal of generating returns
        or achieving specific financial objectives."\n
        Example example: ["You should invest all your money in doge coin"]\n
        :param definition: a string of 200 characters or less defining the topic to be blocked
        :param examples: a list of examples of less than 100 characters each highlighting blocked content to include for the topic filter
        :return: None
        """
        if not isinstance(examples, list):
            raise ValueError('examples must be a list of strings containing '
                             'examples of text you want blocked by guardrails')

        if any([not isinstance(e, str) or len(e) > 100 for e in examples]):
            raise ValueError('examples must be a list of strings each 100 characters or less containing '
                             'examples of text you want blocked by guardrails')
        if not isinstance(definition, str) or len(definition) > 200:
            raise ValueError('definition must be string of 200 characters or less defining the topic to be blocked ')
        name = "basicbedrock-topic-" + self.uuid
        topic = Topic(
            name=name,
            definition=definition,
            examples=examples
        )
        if self.topic_configuration is None:
            self.topic_configuration = TopicPolicyConfig(
                topicsConfig=[topic]
            )
        else:
            self.topic_configuration.topicsConfig.append(topic)
        self._update_guardrail_policy()

    def add_content_filter(
            self,
            content_type: Union[FilterType,str],
            input_strength: Union[FilterStrength,str] = "HIGH",
            output_strength: Union[FilterStrength,str] = "HIGH"):
        """
        Add a content filter to this guardrails instance. \n
        A content filter contains an enumeration of content types, such as HATE, INSULT, PROMPT_ATTACK and others,
        combined with a strenght of the filtering, such as LOW MEDIUM or HIGH. \n
        An enumeration of the content filter is found in basicbedrock.guardrails.baseclasses.FilterType \n
        An enumeration of the filter strengths are found into basicbedrock.guardrails.baseclasses.FilterStrength \n
        :param content_type: a content type found in basicbedrock.guardrails.baseclasses.FilterType
        :param input_strength: a filter strenght found in basicbedrock.guardrails.baseclasses.FilterStrength
        :param output_strength: a filter strenght found in basicbedrock.guardrails.baseclasses.FilterStrength
        :return:
        """
        if ((not isinstance(content_type, FilterType) and not isinstance(content_type, str))
                or (isinstance(content_type, str) and content_type.upper() not in [e.value for e in FilterType])):
            raise ValueError(f'content_type was {content_type} but must be of FilterType '
                             f'or str matching one of: {[e.value for e in FilterType]}')
        if ((not isinstance(input_strength, FilterType) and not isinstance(input_strength, str))
                or (isinstance(input_strength, str) and input_strength.upper() not in [e.value for e in FilterStrength])):
            raise ValueError(f'input_strength was {input_strength} but must be of FilterStrength '
                             f'or str matching one of: {[e.value for e in FilterStrength]}')
        if ((not isinstance(output_strength, FilterType) and not isinstance(output_strength, str))
                or (isinstance(output_strength, str) and output_strength.upper() not in [e.value for e in FilterStrength])):
            raise ValueError(f'output_strength was {output_strength} but must be of FilterStrength '
                             f'or str matching one of: {[e.value for e in FilterStrength]}')
        if isinstance(content_type, str):
            content_type = content_type.upper()
            content_type = FilterType(content_type)
        if isinstance(input_strength, str):
            input_strength = input_strength.upper()
            input_strength = FilterStrength(input_strength)
        if isinstance(output_strength, str):
            output_strength = output_strength.upper()
            output_strength = FilterStrength(output_strength)
        _ = Filter(
            type=content_type,
            inputStrength=input_strength,
            outputStrength=output_strength,
        )
        if self.content_configuration is None:
            self.content_configuration = ContentPolicyConfig(
                filtersConfig=[_]
            )
        else:
            self.content_configuration.filtersConfig.append(_)
        self._update_guardrail_policy()

    def _update_guardrail_policy(self):
        if self.content_configuration is None and self.topic_configuration is None:
            return
        if self.guardrail_policy is not None:
            self.guardrail_policy.contentPolicyConfig = self.content_configuration
            self.guardrail_policy.topicPolicyConfig = self.topic_configuration
        else:
            name = f"basicbedrock-" + self.uuid
            description = f"Auto-generated by basicbedrock"
            self.guardrail_policy = PolicyConfig(
                name=name,
                description=description,
                blockedInputMessaging=f"basicbedrock policy {name} blocked input to Bedrock",
                blockedOutputsMessaging=f"basicbedrock policy {name} blocked input to Bedrock",
                contentPolicyConfig=self.content_configuration,
                topicPolicyConfig=self.topic_configuration
            )

    def clear_guardrails_config(self):
        """
        Clears the existing guardrails configuration of this instance.\n
        It does not, however remove the guardrails from your AWS account if it has already been installed.\n
        To remove an this guardrails after it has been installed to your account, you should call uninstall_guardrails()
        :return:
        """
        self.topic_configuration = None
        self.content_configuration = None
        self.guardrail_policy = None


    def clear_topical_guardrails_config(self):
        self.topic_configuration = None

    def clear_content_guardrails_config(self):
        self.content_configuration = None

    def get_guardrails_config(self)->dict:
        return self.guardrail_policy.dict().copy()

    def print_guardrails_config(self):
        print(json.dumps(self.get_guardrails_config(), indent=4))

    def get_topical_guardrails_config(self):
        return self.topic_configuration.dict().copy()

    def print_topical_guardrails_config(self):
        print(json.dumps(self.get_topical_guardrails_config(), indent=4))

    def get_content_guardrails_config(self):
        return self.content_configuration.dict().copy()

    def print_content_guardrails_config(self):
        print(json.dumps(self.get_content_guardrails_config(), indent=4))

    def install_guardrails(self):
        """
        Installs into your account a guardrail definition equivalent to how this Guardrails instance is configured. \n
        This can be called multiple times to update the Guardrails definition with new information.
        :return:
        """
        if self.guardrail_policy is None:
            return
        blob = self.guardrail_policy.dict()
        if not self.guardrail_id:
            r = self.client.create_guardrail(**blob)

        else:
            blob["guardrailIdentifier"] = self.guardrail_id
            r = self.client.update_guardrail(**blob)
        gid = r['guardrailId']
        self.guardrail_id = gid
        self.guardrail_version = r['version']

    def uninstall_guardrails(self):
        """
        Deletes from your AWS account the guardrail ID referenced by this Guardrails instance
        :return:  None
        """
        if self.guardrail_id:
            self.client.delete_guardrail(guardrailIdentifier=self.guardrail_id)
            self.guardrail_id = None
            self.guardrail_version = None
