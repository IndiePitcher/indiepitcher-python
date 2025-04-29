# IndiePitcher Python SDK

Official Python SDK for [IndiePitcher](https://indiepitcher.com) - email marketing platform for indie hackers.

## Installation

```bash
# Install with pip
pip install indiepitcher

# Or install with uv (recommended)
uv pip install indiepitcher
```

## Quick Start

```python
from indiepitcher import IndiePitcherClient, SendEmail, EmailBodyFormat

# Initialize the client with your API key
client = IndiePitcherClient(api_key="your_api_key")

# Send a transactional email
email = SendEmail(
    to="recipient@example.com",
    subject="Hello from IndiePitcher!",
    body="This is a **markdown** email sent via the IndiePitcher Python SDK.",
    body_format=EmailBodyFormat.MARKDOWN
)

response = client.send_email(email)
print(f"Email sent successfully: {response.success}")
```

## Features

- Send transactional emails with Markdown or HTML content
- Create and manage contacts
- Send emails to contacts or mailing lists
- Create portal sessions for users to manage their subscriptions
- Full Pydantic model support for type safety

## Documentation

For detailed documentation, visit [docs.indiepitcher.com](https://docs.indiepitcher.com).

### Working with Contacts

```python
from indiepitcher import IndiePitcherClient, CreateContact

client = IndiePitcherClient(api_key="your_api_key")

# Create a new contact
contact = CreateContact(
    email="user@example.com",
    name="Example User",
    subscribed_to_lists=["newsletter"],
    custom_properties={"favorite_color": "blue"}
)

response = client.create_contact(contact)

# Get a contact
contact = client.get_contact("user@example.com")
print(contact.data.name)  # "Example User"

# List contacts with pagination
contacts = client.list_contacts(page=1, per_page=50)
for contact in contacts.data:
    print(contact.email)
```

### Sending Emails to Mailing Lists

```python
from indiepitcher import IndiePitcherClient, SendEmailToMailingList, EmailBodyFormat
from datetime import datetime, timedelta

client = IndiePitcherClient(api_key="your_api_key")

# Send an email to a mailing list
email = SendEmailToMailingList(
    subject="Newsletter #1",
    body="# Welcome to our newsletter\n\nThanks for subscribing!",
    body_format=EmailBodyFormat.MARKDOWN,
    list="newsletter",
    track_email_opens=True,
    track_email_link_clicks=True,
    # Schedule the email for future delivery
    delay_until_date=datetime.now() + timedelta(days=1)
)

response = client.send_email_to_mailing_list(email)
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/indiepitcher/indiepitcher-python.git
cd indiepitcher-python

# Install development dependencies with uv (recommended)
uv pip install -e ".[dev]"

# Or with pip
pip install -e ".[dev]"
```

### Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=indiepitcher
```

### Linting

```bash
# Run linter
ruff check .

# Fix linting issues automatically
ruff check --fix .
```

## License

MIT