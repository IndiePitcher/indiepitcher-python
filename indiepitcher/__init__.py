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
    # Models
    "Contact",
    # Response types
    "ContactResponse",
    "ContactsResponse",
    "CreateContact",
    "CreateMailingListPortalSession",
    # Enums
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
]
