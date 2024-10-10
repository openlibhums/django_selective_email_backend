# Django Selective Email Backend

A Django email backend that dynamically selects between Django's SMTP backend and `django_mailgun` based on the sender's email address. Configure specific email addresses to use SMTP while defaulting to Mailgun for all other addresses.

## Features
- Automatically routes emails based on the sender's address.
- Uses SMTP for specific addresses defined in your Django settings.
- Defaults to Mailgun for all other addresses.
- Simple integration with existing Django projects.

## Installation

Install directly from GitHub using `pip`:

```bash
pip install git+https://github.com/yourusername/django-selective-email-backend.git
```

## Configuration

Add the backend to your settings.py:

```python
EMAIL_BACKEND = 'selective_email_backend.backends.SelectiveEmailBackend'
```

Define the SMTP email addresses and other relevant settings:


```python
# settings.py
DEFAULT_EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
SMTP_EMAIL_ADDRESSES = [
    'janeway@janeway.systems',
    'chakotay@janeway.systems',
]

# Mailgun settings
MAILGUN_API_KEY = 'mailgun-api-key'
MAILGUN_DOMAIN = 'mailgun-domain'

# SMTP settings
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-smtp-user'
EMAIL_HOST_PASSWORD = 'your-smtp-password'

```