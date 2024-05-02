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
    """
    SEXUAL = 'SEXUAL'
    VIOLENCE = 'VIOLENCE'
    HATE = 'HATE'
    INSULTS = 'INSULTS'
    MISCONDUCT = 'MISCONDUCT'
    PROMPT_ATTACK = 'PROMPT_ATTACK'
    """
    SEXUAL = 'SEXUAL'
    VIOLENCE = 'VIOLENCE'
    HATE = 'HATE'
    INSULTS = 'INSULTS'
    MISCONDUCT = 'MISCONDUCT'
    PROMPT_ATTACK = 'PROMPT_ATTACK'


class FilterStrength(enum.Enum):
    """
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    NONE = 'NONE'
    """
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    NONE = 'NONE'


class Topic(BotoizerBaseModel):
    """
    name: str
    definition: str
    examples: List[str]
    type: str = "DENY"
    """
    name: str
    definition: str
    examples: List[str]
    type: str = "DENY"


class TopicPolicyConfig(BotoizerBaseModel):
    """
    topicsConfig: List[Topic]
    """
    topicsConfig: List[Topic]


class Filter(BotoizerBaseModel):
    """
    type: FilterType
    inputStrength: FilterStrength
    outputStrength: FilterStrength
    """
    type: FilterType
    inputStrength: FilterStrength
    outputStrength: FilterStrength


class ContentPolicyConfig(BotoizerBaseModel):
    """
    filtersConfig: List[Filter]
    """
    filtersConfig: List[Filter]


class WordConfig(BotoizerBaseModel):
    """
    text: str
    """
    text: str


class ManagedWordListConfig(BotoizerBaseModel):
    """
    text: str
    """
    type: str


class WordPolicyConfig(BotoizerBaseModel):
    """
    wordsConfig: List[WordConfig]
    managedWordListsConfig: List[ManagedWordListConfig]
    """
    wordsConfig: List[WordConfig]
    managedWordListsConfig: List[ManagedWordListConfig]


class PiiEntityConfig(BotoizerBaseModel):
    """
    type: str
    action: str
    """
    type: str
    action: str


class RegexConfig(BotoizerBaseModel):
    """
    name: str
    description: str
    pattern: str
    action: str
    """
    name: str
    description: str
    pattern: str
    action: str


class SensitiveInformationPolicyConfig(BotoizerBaseModel):
    """
    piiEntitiesConfig: List[PiiEntityConfig]
    regexesConfig: List[RegexConfig]
    """
    piiEntitiesConfig: List[PiiEntityConfig]
    regexesConfig: List[RegexConfig]


class Tag(BotoizerBaseModel):
    """
    key: str
    value: str
    """
    key: str
    value: str


class PolicyConfig(BotoizerBaseModel):
    """
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
    """
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
