from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend as SMTPBackend
from django.utils.module_loading import import_string
from email.utils import parseaddr


class SelectiveEmailBackend:
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        self.default_backend = import_string(
            getattr(settings, 'DEFAULT_EMAIL_BACKEND')
        )(
            *args,
            **kwargs,
        )
        self.smtp_backends = {}
        self.base_args = args
        self.base_kwargs = kwargs

    def _get_smtp_backend_for(self, email):
        config = settings.MULTI_SMTP_CONFIG.get(email.lower())

        if not config:
            return self.default_backend

        if email.lower() not in self.smtp_backends:
            self.smtp_backends[email.lower()] = SMTPBackend(
                host=config.get("EMAIL_HOST"),
                port=config.get("EMAIL_PORT"),
                username=config.get("EMAIL_HOST_USER"),
                password=config.get("EMAIL_HOST_PASSWORD"),
                use_tls=config.get("EMAIL_USE_TLS", False),
                use_ssl=config.get("EMAIL_USE_SSL", False),
                timeout=config.get("EMAIL_TIMEOUT", None),
                ssl_keyfile=config.get("EMAIL_SSL_KEYFILE", None),
                ssl_certfile=config.get("EMAIL_SSL_CERTFILE", None),
            )

        return self.smtp_backends[email.lower()]

    def send_messages(self, email_messages):
        for message in email_messages:
            name, email = parseaddr(message.from_email)
            backend = self._get_smtp_backend_for(email) or self.default_backend
            backend.send_messages([message])
