"""" Suppose we have a NotificationService class that is responsible for sending notifications. The NotificationService 
class directly depends on the EmailSender class to send emails. In this implementation, the NotificationService class directly 
depends on the EmailSender class, which violates the Dependency Inversion Principle. The high-level NotificationService should 
not depend on the low-level EmailSender, as it tightly couples the classes together."""

from abc import ABC, abstractmethod

class EmailServer(ABC):
    @abstractmethod
    def send_email(self, recipient, message):
        pass

class EmailSender(EmailServer):
    def send_email(self, recipient, subject, message):
        print(f"Sending email to {recipient}: {subject} - {message}")

class NotificationService():
    def __init__(self):
        self.email_sender = EmailSender()

    def send_notification(self, recipient, message):
        self.email_sender.send_email(recipient, "Notification", message)

notification_service = NotificationService()
notification_service.send_notification("demo@example.com", "Hello demo, this is a notification!")
