# Django Selective Email Backend

A Django email backend that dynamically selects between Django's SMTP backend and a configurable email backend based on the sender's email address. Configure specific email addresses to use SMTP while falling back to a default backend for all other addresses.

## Features
- Automatically routes emails based on the sender's address.
- Uses SMTP for specific addresses defined in your Django settings.
- Defaults to a configurable backend (eg django_mailgun) for all other addresses.
- Simple integration with existing Django projects.

## Installation

Install directly from GitHub using `pip`:

```bash
pip install -e git+ssh://git@github.com/openlibhums/django_selective_email_backend@v0.0.2#egg=django-selective-email-backend
```

## Configuration

Add the backend to your settings.py:

```python
EMAIL_BACKEND = 'selective_email_backend.backends.SelectiveEmailBackend'
```

Define the SMTP email addresses and other relevant settings:


```python
# settings.py
INSTALLED_APPS = [
    ...
    'selective_email_backend',
    ...
]

DEFAULT_EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
SMTP_EMAIL_ADDRESSES = [
    'janeway@janeway.systems',
    'chakotay@janeway.systems',
]

# Mailgun settings
MAILGUN_ACCESS_KEY = 'mailgun-access-key'
MAILGUN_SERVER_NAME = 'mailgun-server-name'

# SMTP settings
EMAIL_HOST = 'smtp.janeway.systems'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'smtp-user-name'
EMAIL_HOST_PASSWORD = 'smtp-password'

```