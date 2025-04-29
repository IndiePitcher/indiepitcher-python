"""Tests for IndiePitcher client."""

import pytest
import responses
from responses import matchers

from indiepitcher import CreateContact, EmailBodyFormat, IndiePitcherClient, SendEmail


@pytest.fixture
def client():
    """Create a test client."""
    return IndiePitcherClient(api_key="test_api_key")


@responses.activate
def test_get_contact(client):
    """Test getting a contact by email."""
    responses.add(
        responses.GET,
        "https://api.indiepitcher.com/v1/contacts/find",
        json={
            "success": True,
            "data": {
                "email": "test@example.com",
                "name": "Test User",
                "userId": "123",
                "subscribedToLists": ["list1"],
            },
        },
        match=[matchers.query_param_matcher({"email": "test@example.com"})],
        status=200,
    )

    response = client.get_contact("test@example.com")

    assert response.success is True
    assert response.data.email == "test@example.com"
    assert response.data.name == "Test User"
    assert response.data.user_id == "123"
    assert response.data.subscribed_to_lists == ["list1"]


@responses.activate
def test_create_contact(client):
    """Test creating a contact."""
    responses.add(
        responses.POST,
        "https://api.indiepitcher.com/v1/contacts/create",
        json={
            "success": True,
            "data": {
                "email": "new@example.com",
                "name": "New User",
                "userId": "456",
                "subscribedToLists": ["list1"],
            },
        },
        match=[
            matchers.json_params_matcher(
                {
                    "email": "new@example.com",
                    "name": "New User",
                    "userId": "456",
                    "subscribedToLists": ["list1"],
                }
            )
        ],
        status=200,
    )

    contact = CreateContact(
        email="new@example.com", name="New User", user_id="456", subscribed_to_lists=["list1"]
    )

    response = client.create_contact(contact)

    assert response.success is True
    assert response.data.email == "new@example.com"
    assert response.data.name == "New User"


@responses.activate
def test_send_email(client):
    """Test sending an email."""
    responses.add(
        responses.POST,
        "https://api.indiepitcher.com/v1/email/transactional",
        json={"success": True, "data": None},
        match=[
            matchers.json_params_matcher(
                {
                    "to": "recipient@example.com",
                    "subject": "Test Email",
                    "body": "Hello world",
                    "bodyFormat": "markdown",
                }
            )
        ],
        status=200,
    )

    email = SendEmail(
        to="recipient@example.com",
        subject="Test Email",
        body="Hello world",
        body_format=EmailBodyFormat.MARKDOWN,
    )

    response = client.send_email(email)

    assert response.success is True
