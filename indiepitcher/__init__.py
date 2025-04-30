"""IndiePitcher Python SDK for email marketing platform."""

from .client import IndiePitcherClient
from .models import (  # Models; Response types; Enums
    Contact,
    ContactResponse,
    ContactsResponse,
    CreateContact,
    CreateMailingListPortalSession,
    EmailBodyFormat,
    EmptyResponse,
    IndiePitcherResponseError,
    MailingList,
    MailingListPortalSession,
    MailingListPortalSessionResponse,
    MailingListsResponse,
    SendEmail,
    SendEmailToContact,
    SendEmailToMailingList,
    UpdateContact,
)

__all__ = [
    "Contact",
    "ContactResponse",
    "ContactsResponse",
    "CreateContact",
    "CreateMailingListPortalSession",
    "EmailBodyFormat",
    "EmptyResponse",
    "IndiePitcherClient",
    "MailingList",
    "MailingListPortalSession",
    "MailingListPortalSessionResponse",
    "MailingListsResponse",
    "SendEmail",
    "SendEmailToContact",
    "SendEmailToMailingList",
    "UpdateContact",
    "IndiePitcherResponseError",
]
