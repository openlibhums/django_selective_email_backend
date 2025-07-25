# Django Selective Email Backend

A Django email backend that dynamically selects between multiple SMTP backends and a configurable default backend based on the sender's email address. Configure per-sender SMTP settings in your Django settings, and fall back to a default backend (e.g. `django_mailgun`) for all other addresses.

## Features

- Automatically routes emails based on the sender's address.
- Supports multiple SMTP configurations mapped to specific email addresses.
- Defaults to a configurable backend (e.g. `django_mailgun`) for all other addresses.
- Simple integration with existing Django projects.

## Installation

Install directly from GitHub using `pip`:

```bash
pip install git+ssh://git@github.com/openlibhums/django_selective_email_backend@v0.1#egg=django-selective-email-backend
```

## Configuration

Add the backend to your `settings.py`:

```python
EMAIL_BACKEND = 'selective_email_backend.backends.SelectiveEmailBackend'
```

Configure a default backend and per-address SMTP settings:

```python
# settings.py
INSTALLED_APPS = [
    ...
    'selective_email_backend',
    ...
]

DEFAULT_EMAIL_BACKEND = 'django_mailgun.MailgunBackend'

# Mailgun settings (default backend)
MAILGUN_ACCESS_KEY = 'mailgun-access-key'
MAILGUN_SERVER_NAME = 'mailgun-server-name'

# Multi-SMTP settings (per-sender)
MULTI_SMTP_CONFIG = {
    'janeway@janeway.systems': {
        'EMAIL_HOST': 'smtp.janeway.systems',
        'EMAIL_PORT': 587,
        'EMAIL_HOST_USER': 'janeway@janeway.systems',
        'EMAIL_HOST_PASSWORD': 'smtp-password-janeway',
        'EMAIL_USE_TLS': True,
    },
    'chakotay@janeway.systems': {
        'EMAIL_HOST': 'smtp.janeway.systems',
        'EMAIL_PORT': 587,
        'EMAIL_HOST_USER': 'chakotay@janeway.systems',
        'EMAIL_HOST_PASSWORD': 'smtp-password-chakotay',
        'EMAIL_USE_TLS': True,
    },
}
```

## Notes

- Email addresses in `MULTI_SMTP_CONFIG` are matched case-insensitively.
- All addresses not listed in `MULTI_SMTP_CONFIG` will use the backend specified by `DEFAULT_EMAIL_BACKEND`.
