"""Tests for IndiePitcher client."""

import os
import time

import pytest
from dotenv import load_dotenv

from indiepitcher import IndiePitcherClient

# Load environment variables from .env file
load_dotenv()


@pytest.fixture
def client():
    """Create a test client with API key from environment."""
    api_key = os.environ.get("INDIEPITCHER_API_KEY", "test_api_key")
    return IndiePitcherClient(api_key=api_key)


@pytest.fixture(autouse=True)
def sleep_after_test():
    """Sleep for 1 second after each test."""
    yield  # This allows the test to run
    time.sleep(1)  # Then sleeps for 1 second after the test completes


def test_list_mailing_lists(client):
    """Test listing mailing lists."""

    response = client.list_mailing_lists()
    assert len(response.data) == 3


# def test_get_contact(client):
#     """Test getting a contact by email."""

#     response = client.get_contact("test@example.com")

#     assert response.success is True
#     assert response.data.email == "test@example.com"
#     assert response.data.name == "Test User"
#     assert response.data.user_id == "123"
#     assert response.data.subscribed_to_lists == ["list1"]


# def test_create_contact(client):
#     """Test creating a contact."""

#     contact = CreateContact(
#         email="new@example.com",
#         name="New User",
#         user_id="456",
#         subscribed_to_lists=["list1"],
#     )

#     response = client.create_contact(contact)

#     assert response.success is True
#     assert response.data.email == "new@example.com"
#     assert response.data.name == "New User"


# def test_send_email(client):
#     """Test sending an email."""

#     email = SendEmail(
#         to="recipient@example.com",
#         subject="Test Email",
#         body="Hello world",
#         body_format=EmailBodyFormat.MARKDOWN,
#     )

#     response = client.send_email(email)

#     assert response.success is True
