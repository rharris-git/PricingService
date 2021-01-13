

import os
from typing import List
from requests import Response, post


class MailgunException(Exception):
    def __init__(self, message: str):
        self.message = message


class Mailgun:

    @classmethod
    def send_mail(cls, email: List[str], subject: str, text: str, html: str) -> Response:

        mailgun_api_key = os.environ.get('MAILGUN_API_KEY', None)
        mailgun_domain = os.environ.get('MAILGUN_DOMAIN', None)

        from_title = os.environ.get('FROM_TITLE', None)
        from_email = os.environ.get('FROM_EMAIL', None)

        if mailgun_api_key is None:
            raise MailgunException("Failed to load MAILGUN_API_KEY.")
        if mailgun_domain is None:
            raise MailgunException("Failed to load MAILGUN_DOMAIN.")
        if from_title is None:
            raise MailgunException("Failed to load FROM_TITLE.")
        if from_email is None:
            raise MailgunException("Failed to load FROM_EMAIL.")

        response = post(
            f"{mailgun_domain}/messages",
            auth=("api", mailgun_api_key),
            data={"from": f"{from_title} <{from_email}>",
                "to": email,
                "subject": subject,
                "text": text,
                "html": html
            }
        )

        if response.status_code != 200:
            raise MailgunException('An error occurred while sending email')
        return response


