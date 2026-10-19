
import json
import urllib.request
import urllib.error

from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend


class BrevoEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        if not email_messages:
            return 0

        api_key = getattr(settings, "BREVO_API_KEY", "")
        if not api_key:
            raise ValueError("La variable BREVO_API_KEY est absente.")

        sent = 0

        for message in email_messages:
            sender = message.from_email or settings.DEFAULT_FROM_EMAIL

            payload = {
                "sender": {
                    "name": "DORTOIR MADI",
                    "email": sender,
                },
                "to": [{"email": address} for address in message.to],
                "subject": message.subject or "",
            }

            html_content = None
            for alternative in getattr(message, "alternatives", []):
                if getattr(alternative, "mimetype", "") == "text/html":
                    html_content = alternative.content
                    break

            if html_content is not None:
                payload["htmlContent"] = html_content
            else:
                payload["textContent"] = message.body or ""

            request = urllib.request.Request(
                "https://api.brevo.com/v3/smtp/email",
                data=json.dumps(payload).encode("utf-8"),
                headers={
                    "api-key": api_key,
                    "accept": "application/json",
                    "content-type": "application/json",
                },
                method="POST",
            )

            try:
                with urllib.request.urlopen(request, timeout=25) as response:
                    if 200 <= response.status < 300:
                        sent += 1
            except urllib.error.HTTPError as error:
                details = error.read().decode("utf-8", errors="replace")
                raise RuntimeError(
                    f"Erreur API Brevo HTTP {error.code}: {details}"
                ) from error
            except urllib.error.URLError as error:
                raise RuntimeError(
                    f"Connexion HTTPS à Brevo impossible: {error.reason}"
                ) from error

        return sent
