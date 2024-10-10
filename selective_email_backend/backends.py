from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend as SMTPBackend
from django.utils.module_loading import import_string


class SelectiveEmailBackend:
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        self.smtp_backend = SMTPBackend(
            *args,
            **kwargs,
        )
        default_backend_path = getattr(
            settings, 
            'DEFAULT_EMAIL_BACKEND', 
        )
        DefaultBackendClass = import_string(default_backend_path)
        self.default_backend = DefaultBackendClass(
            *args,
            **kwargs,
        )

    def send_messages(self, email_messages):
        smtp_addresses = getattr(settings, 'SMTP_EMAIL_ADDRESSES', [])

        for message in email_messages:
            if message.from_email.lower() in (addr.lower() for addr in smtp_addresses):
                backend = self.smtp_backend
            else:
                backend = self.default_backend
            
            backend.send_messages([message])