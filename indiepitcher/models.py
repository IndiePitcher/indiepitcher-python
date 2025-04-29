from datetime import datetime
from enum import Enum
from typing import Any, Dict, Generic, List, Optional, TypeVar

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel, to_snake

T = TypeVar("T")
M = TypeVar("M", bound=Dict[str, Any])


class EmailBodyFormat(str, Enum):
    """Format of the email body content."""

    MARKDOWN = "markdown"
    HTML = "html"


class BaseIndiePitcherResponseModel(BaseModel):
    """Base model with configuration for all IndiePitcher response models."""

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=to_camel,
        arbitrary_types_allowed=True,
    )


class BaseIndiePitcherRequestModel(BaseModel):
    """Base model with configuration for all IndiePitcher response models."""

    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=to_snake,
        arbitrary_types_allowed=True,
    )


class Response(BaseIndiePitcherResponseModel, Generic[T]):
    """Generic response wrapper for API responses with data."""

    success: bool
    data: T


class PaginationMetadata(BaseIndiePitcherResponseModel):
    """Standard pagination metadata."""

    page: int
    per: int
    total: int


class PaginatedResponse(BaseIndiePitcherResponseModel, Generic[T]):
    """Generic response wrapper for paginated API responses."""

    success: bool
    data: List[T]
    metadata: PaginationMetadata


class Contact(BaseIndiePitcherResponseModel):
    """Represents a contact in the IndiePitcher system."""

    email: str
    user_id: Optional[str] = None
    name: Optional[str] = None
    avatar_url: Optional[str] = None
    language_code: Optional[str] = None
    hard_bounced_at: Optional[datetime] = None
    subscribed_to_lists: List[str] = Field(default_factory=list)
    custom_properties: Dict[str, Any] = Field(default_factory=dict)


class CreateContact(BaseIndiePitcherRequestModel):
    """Data for creating a new contact."""

    email: str
    user_id: Optional[str] = None
    avatar_url: Optional[str] = None
    name: Optional[str] = None
    language_code: Optional[str] = None
    update_if_exists: Optional[bool] = None
    ignore_list_subscriptions_when_updating: Optional[bool] = None
    subscribed_to_lists: List[str] = Field(default_factory=list)
    custom_properties: Dict[str, Any] = Field(default_factory=dict)


class UpdateContact(BaseIndiePitcherRequestModel):
    """Data for updating an existing contact."""

    email: str
    user_id: Optional[str] = None
    avatar_url: Optional[str] = None
    name: Optional[str] = None
    language_code: Optional[str] = None
    added_list_subscripitons: Optional[List[str]] = None
    removed_list_subscripitons: Optional[List[str]] = None
    custom_properties: Optional[Dict[str, Any]] = None


class MailingList(BaseIndiePitcherResponseModel):
    """Represents a mailing list in the IndiePitcher system."""

    name: str
    title: str
    num_subscribers: int


class CreateMailingListPortalSession(BaseIndiePitcherRequestModel):
    """Data for creating a mailing list portal session."""

    contact_email: str
    return_url: str


class MailingListPortalSession(BaseIndiePitcherResponseModel):
    """Response from creating a mailing list portal session."""

    url: str
    expires_at: datetime
    return_url: str


class SendEmail(BaseIndiePitcherRequestModel):
    """Data for sending a transactional email."""

    to: str
    subject: str
    body: str
    body_format: EmailBodyFormat
    track_email_opens: Optional[bool] = None
    track_email_link_clicks: Optional[bool] = None


class SendEmailToContact(BaseIndiePitcherRequestModel):
    """Data for sending an email to a contact or contacts."""

    subject: str
    body: str
    body_format: EmailBodyFormat
    list: str
    contact_email: Optional[str] = None
    contact_emails: Optional[List[str]] = None
    delay_seconds: Optional[float] = None
    delay_until_date: Optional[datetime] = None
    track_email_opens: Optional[bool] = None
    track_email_link_clicks: Optional[bool] = None


class SendEmailToMailingList(BaseIndiePitcherRequestModel):
    """Data for sending an email to a mailing list."""

    subject: str
    body: str
    body_format: EmailBodyFormat
    list: str
    delay_seconds: Optional[float] = None
    delay_until_date: Optional[datetime] = None
    track_email_opens: Optional[bool] = None
    track_email_link_clicks: Optional[bool] = None


# Type aliases for common response types
ContactResponse = Response[Contact]
EmptyResponse = Response[None]
ContactsResponse = PaginatedResponse[Contact]
MailingListsResponse = PaginatedResponse[MailingList]
MailingListPortalSessionResponse = Response[MailingListPortalSession]
