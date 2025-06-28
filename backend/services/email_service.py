import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment
from utils.config import settings
from utils.logger import logger

def send_travel_documents(email: str, subject: str, content: str, attachments: list = []) -> bool:
    """Sends email with travel documents"""
    try:
        message = Mail(
            from_email=settings.email_from,
            to_emails=email,
            subject=subject,
            html_content=content
        )
        
        for file in attachments:
            with open(file['path'], 'rb') as f:
                data = f.read()
            attachment = Attachment(
                file_content=FileContent(data),
                file_name=file['name'],
                file_type=file['type'],
                disposition='attachment'
            )
            message.attachment = attachment
        
        sg = SendGridAPIClient(settings.sendgrid_key)
        response = sg.send(message)
        return response.status_code == 202
    except Exception as e:
        logger.error(f"Email failed: {str(e)}")
        return False