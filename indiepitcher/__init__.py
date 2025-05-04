"""IndiePitcher Python SDK for email marketing platform."""

from .client import IndiePitcherClient
from .models import (  # Models; Response types; Enums
    Contact,
    CreateContact,
    CreateMailingListPortalSession,
    EmailBodyFormat,
    EmptyResponse,
    IndiePitcherResponseError,
    MailingList,
    MailingListPortalSession,
    SendEmail,
    SendEmailToContact,
    SendEmailToMailingList,
    UpdateContact,
)

__all__ = [
    "Contact",
    "CreateContact",
    "CreateMailingListPortalSession",
    "EmailBodyFormat",
    "EmptyResponse",
    "IndiePitcherClient",
    "MailingList",
    "MailingListPortalSession",
    "SendEmail",
    "SendEmailToContact",
    "SendEmailToMailingList",
    "UpdateContact",
    "IndiePitcherResponseError",
]
