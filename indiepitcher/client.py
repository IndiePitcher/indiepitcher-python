from typing import List

import requests

from .models import (
    ContactResponse,
    ContactsResponse,
    CreateContact,
    CreateMailingListPortalSession,
    EmptyResponse,
    MailingListPortalSessionResponse,
    MailingListsResponse,
    SendEmail,
    SendEmailToContact,
    SendEmailToMailingList,
    UpdateContact,
)


class IndiePitcherClient:
    """Client for interacting with the IndiePitcher API."""

    def __init__(
        self, api_key: str, base_url: str = "https://api.indiepitcher.com/v1"
    ) -> None:
        """
        Initialize the IndiePitcher API client.

        Args:
            api_key: Your IndiePitcher API key
            base_url: Base URL for the IndiePitcher API (default: https://api.indiepitcher.com/v1)
        """
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "User-Agent": "IndiePitcher-Python/0.1.0",
            }
        )

    # Contact Management

    def get_contact(self, email: str) -> ContactResponse:
        """
        Find a contact by email.

        Args:
            email: The email address of the contact to find

        Returns:
            ContactResponse: The contact if found

        Raises:
            requests.HTTPError: If the request fails
        """
        response = self.session.get(
            f"{self.base_url}/contacts/find", params={"email": email}
        )
        response.raise_for_status()
        return ContactResponse.model_validate_json(response.content)

    def list_contacts(self, page: int = 1, per_page: int = 50) -> ContactsResponse:
        """
        List contacts with pagination.

        Args:
            page: Page number (default: 1)
            per_page: Number of contacts per page (default: 50)

        Returns:
            ContactsResponse: Paginated list of contacts

        Raises:
            requests.HTTPError: If the request fails
        """
        response = self.session.get(
            f"{self.base_url}/contacts", params={"page": page, "per": per_page}
        )
        response.raise_for_status()
        return ContactsResponse.model_validate_json(response.content)

    def create_contact(self, contact: CreateContact) -> ContactResponse:
        """
        Add a new contact.

        Args:
            contact: Contact details to create

        Returns:
            ContactResponse: The created contact

        Raises:
            requests.HTTPError: If the request fails
        """
        response = self.session.post(
            f"{self.base_url}/contacts/create",
            json=contact.model_dump(by_alias=True, exclude_none=True),
        )
        response.raise_for_status()
        return ContactResponse.model_validate_json(response.content)

    def create_contacts(self, contacts: List[CreateContact]) -> ContactsResponse:
        """
        Add multiple contacts in a single request.

        Args:
            contacts: List of contacts to create (max 100)

        Returns:
            ContactsResponse: The created contacts

        Raises:
            requests.HTTPError: If the request fails
            ValueError: If more than 100 contacts are provided
        """
        if len(contacts) > 100:
            raise ValueError("Maximum 100 contacts can be created in a single request")

        response = self.session.post(
            f"{self.base_url}/contacts/create_many",
            json=[
                contact.model_dump(by_alias=True, exclude_none=True)
                for contact in contacts
            ],
        )
        response.raise_for_status()
        return ContactsResponse.model_validate_json(response.content)

    def update_contact(self, contact: UpdateContact) -> ContactResponse:
        """
        Update an existing contact.

        Args:
            contact: Contact details to update

        Returns:
            ContactResponse: The updated contact

        Raises:
            requests.HTTPError: If the request fails
        """
        response = self.session.patch(
            f"{self.base_url}/contacts/update",
            json=contact.model_dump(by_alias=True, exclude_none=True),
        )
        response.raise_for_status()
        return ContactResponse.model_validate_json(response.content)

    def delete_contact(self, email: str) -> EmptyResponse:
        """
        Delete a contact by email.

        Args:
            email: Email address of the contact to delete

        Returns:
            EmptyResponse: Success response

        Raises:
            requests.HTTPError: If the request fails
        """
        response = self.session.post(
            f"{self.base_url}/contacts/delete", json={"email": email}
        )
        response.raise_for_status()
        return EmptyResponse.model_validate_json(response.content)

    # Mailing List Management

    def list_mailing_lists(
        self, page: int = 1, per_page: int = 10
    ) -> MailingListsResponse:
        """
        Get all mailing lists.

        Args:
            page: Page number (default: 1)
            per_page: Number of lists per page (default: 10)

        Returns:
            MailingListsResponse: Paginated list of mailing lists

        Raises:
            requests.HTTPError: If the request fails
        """
        response = self.session.get(
            f"{self.base_url}/lists", params={"page": page, "per": per_page}
        )
        response.raise_for_status()
        return MailingListsResponse.model_validate_json(response.content)

    def create_mailing_list_portal_session(
        self, session: CreateMailingListPortalSession
    ) -> MailingListPortalSessionResponse:
        """
        Create a mailing list portal session.

        Args:
            session: Portal session details

        Returns:
            MailingListPortalSessionResponse: Portal session details with URL

        Raises:
            requests.HTTPError: If the request fails
        """
        response = self.session.post(
            f"{self.base_url}/lists/portal_session",
            json=session.model_dump(by_alias=True, exclude_none=True),
        )
        response.raise_for_status()
        return MailingListPortalSessionResponse.model_validate_json(response.content)

    # Email Sending

    def send_email(self, email: SendEmail) -> EmptyResponse:
        """
        Send a transactional email.

        Args:
            email: Email details to send

        Returns:
            EmptyResponse: Success response

        Raises:
            requests.HTTPError: If the request fails
        """
        response = self.session.post(
            f"{self.base_url}/email/transactional",
            json=email.model_dump(by_alias=True, exclude_none=True),
        )
        response.raise_for_status()
        return EmptyResponse.model_validate_json(response.content)

    def send_email_to_contact(self, email: SendEmailToContact) -> EmptyResponse:
        """
        Send an email to one or more contacts.

        Args:
            email: Email details to send

        Returns:
            EmptyResponse: Success response

        Raises:
            requests.HTTPError: If the request fails
        """
        response = self.session.post(
            f"{self.base_url}/email/contact",
            json=email.model_dump(by_alias=True, exclude_none=True),
        )
        response.raise_for_status()
        return EmptyResponse.model_validate_json(response.content)

    def send_email_to_mailing_list(
        self, email: SendEmailToMailingList
    ) -> EmptyResponse:
        """
        Send an email to a mailing list.

        Args:
            email: Email details to send

        Returns:
            EmptyResponse: Success response

        Raises:
            requests.HTTPError: If the request fails
        """
        response = self.session.post(
            f"{self.base_url}/email/list",
            json=email.model_dump(by_alias=True, exclude_none=True),
        )
        response.raise_for_status()
        return EmptyResponse.model_validate_json(response.content)
