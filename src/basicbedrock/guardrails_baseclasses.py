"""
Contains all of the base classes for working with guardrails

reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_guardrail.html

Example:
```
    session = boto3.session.Session()
    client = session.client('bedrock')

    filter = Filter(
        type="SEXUAL",
        inputStrength="LOW",
        outputStrength="MEDIUM",
    )
    content_policy = ContentPolicyConfig(
        filtersConfig=[filter]
    )

    policy = PolicyConfig(
        name="b",
        description="c",
        blockedInputMessaging="stopped on input",
        blockedOutputsMessaging="stopped on output",
        contentPolicyConfig=content_policy
    ).dict()

    print(f"Creating: {policy}")
    r = client.create_guardrail(**policy)
    gid = r['guardrailId']
    client.delete_guardrail(guardrailIdentifier=gid)
```
"""
from typing import List, Optional
from pydantic import BaseModel, model_validator
import enum
from typing_extensions import Self


class BotoizerBaseModel(BaseModel, extra="forbid", use_enum_values=True):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dict(self, *args, **kwargs) -> dict:
        """
        override default dict behavior.  boto3 does not want None or null values, we need to exclude them from building
        This function overrides so that the default behaviour is to exclude_none=True
        :param args: args passed onto BaseModel.dict()
        :param kwargs: kwargs passed onto BaseModel.dict()
        :return: model dict suitable for boto3
        """
        if 'exclude_none' in kwargs:
            return super().dict(*args, **kwargs)
        else:
            return super().dict(*args, exclude_none=True, **kwargs)

    def json(self, *args, **kwargs) -> str:
        """
        override default json behavior.  boto3 does not want None or null values, we need to exclude them from building
        This function overrides so that the default behaviour is to exclude_none=True
        :param args: args passed onto BaseModel.json()
        :param kwargs: kwargs passed onto BaseModel.json()
        :return: model json suitable for boto3
        """
        if 'exclude_none' in kwargs:
            return super().json(*args, **kwargs)
        else:
            return super().json(*args, exclude_none=True, **kwargs)


class FilterType(enum.Enum):
    SEXUAL = 'SEXUAL'
    VIOLENCE = 'VIOLENCE'
    HATE = 'HATE'
    INSULTS = 'INSULTS'
    MISCONDUCT = 'MISCONDUCT'
    PROMPT_ATTACK = 'PROMPT_ATTACK'

    def __init__(self, *args, **kwargs):
        """
        SEXUAL = 'SEXUAL'\n
        VIOLENCE = 'VIOLENCE'\n
        HATE = 'HATE'\n
        INSULTS = 'INSULTS'\n
        MISCONDUCT = 'MISCONDUCT'\n
        PROMPT_ATTACK = 'PROMPT_ATTACK'\n
        """
        super().__init__()


class FilterStrength(enum.Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    NONE = 'NONE'

    def __init__(self, *args, **kwargs):
        """
        LOW = 'LOW'\n
        MEDIUM = 'MEDIUM'\n
        HIGH = 'HIGH'\n
        NONE = 'NONE'\n
        """
        super().__init__()


class Topic(BotoizerBaseModel):
    name: str
    definition: str
    examples: List[str]
    type: str = "DENY"

    def __init__(self, *args, **kwargs):
        """
        name: str\n
        definition: str\n
        examples: List[str]\n
        type: str = "DENY"\n
        """
        super().__init__(*args, **kwargs)


class TopicPolicyConfig(BotoizerBaseModel):
    topicsConfig: List[Topic]

    def __init__(self, *args, **kwargs):
        """
        topicsConfig: List[Topic]\n
        """
        super().__init__(*args, **kwargs)


class Filter(BotoizerBaseModel):
    type: FilterType
    inputStrength: FilterStrength
    outputStrength: FilterStrength

    def __init__(self, *args, **kwargs):
        """
        type: FilterType\n
        inputStrength: FilterStrength\n
        outputStrength: FilterStrength\n
        """
        super().__init__(*args, **kwargs)


class ContentPolicyConfig(BotoizerBaseModel):
    filtersConfig: List[Filter]

    def __init__(self, *args, **kwargs):
        """
        filtersConfig: List[Filter]\n
        """
        super().__init__(*args, **kwargs)


class WordConfig(BotoizerBaseModel):
    text: str

    def __init__(self, *args, **kwargs):
        """
        text: str\n
        """
        super().__init__(*args, **kwargs)


class ManagedWordListConfig(BotoizerBaseModel):
    type: str

    def __init__(self, *args, **kwargs):
        """
        text: str\n
        """
        super().__init__(*args, **kwargs)


class WordPolicyConfig(BotoizerBaseModel):
    wordsConfig: List[WordConfig]
    managedWordListsConfig: List[ManagedWordListConfig]

    def __init__(self, *args, **kwargs):
        """
        wordsConfig: List[WordConfig]\n
        managedWordListsConfig: List[ManagedWordListConfig]\n
        """
        super().__init__(*args, **kwargs)


class PiiEntityConfig(BotoizerBaseModel):
    type: str
    action: str

    def __init__(self, *args, **kwargs):
        """
        type: str\n
        action: str\n
        """
        super().__init__(*args, **kwargs)


class RegexConfig(BotoizerBaseModel):
    name: str
    description: str
    pattern: str
    action: str

    def __init__(self, *args, **kwargs):
        """
        name: str\n
        description: str\n
        pattern: str\n
        action: str\n
        """
        super().__init__(*args, **kwargs)


class SensitiveInformationPolicyConfig(BotoizerBaseModel):
    piiEntitiesConfig: List[PiiEntityConfig]
    regexesConfig: List[RegexConfig]

    def __init__(self, *args, **kwargs):
        """
        piiEntitiesConfig: List[PiiEntityConfig]\n
        regexesConfig: List[RegexConfig]\n
        """
        super().__init__(*args, **kwargs)


class Tag(BotoizerBaseModel):
    key: str
    value: str

    def __init__(self, *args, **kwargs):
        """
        key: str\n
        value: str\n
        """
        super().__init__(*args, **kwargs)


class PolicyConfig(BotoizerBaseModel):
    name: str
    description: str
    topicPolicyConfig: Optional[TopicPolicyConfig] = None
    contentPolicyConfig: Optional[ContentPolicyConfig] = None
    wordPolicyConfig: Optional[WordPolicyConfig] = None
    sensitiveInformationPolicyConfig: Optional[SensitiveInformationPolicyConfig] = None
    blockedInputMessaging: str = None
    blockedOutputsMessaging: str = None
    kmsKeyId: Optional[str] = None
    tags: Optional[List[Tag]] = None
    clientRequestToken: Optional[str] = None

    @model_validator(mode='after')
    def minimim_policy_validator(self) -> Self:
        if not self.topicPolicyConfig and not self.contentPolicyConfig:
            raise ValueError("A guardrail must have at least one policy configured, and you have none. You must "
                             "create at least one topic policy or one content policy")
        return self

    def __init__(self, *args, **kwargs):
        """
        name: str\n
        description: str\n
        topicPolicyConfig: Optional[TopicPolicyConfig] = None\n
        contentPolicyConfig: Optional[ContentPolicyConfig] = None\n
        wordPolicyConfig: Optional[WordPolicyConfig] = None\n
        sensitiveInformationPolicyConfig: Optional[SensitiveInformationPolicyConfig] = None\n
        blockedInputMessaging: str = None\n
        blockedOutputsMessaging: str = None\n
        kmsKeyId: Optional[str] = None\n
        tags: Optional[List[Tag]] = None\n
        clientRequestToken: Optional[str] = None\n
        """
        super().__init__(*args, **kwargs)