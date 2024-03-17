# high level module should not depend upon low level both depend uopn abstraction/interface
# the abstraction not depend uopn details(concrete implementaion) and details(concrete implementaion) depend uopn abstraction 

from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

class EmailService(NotificationService):
    def send_notification(self, message):
        print(f"Sending email: {message}")

class SMSService(NotificationService):
    def send_notification(self, message):
        print(f"Sending SMS: {message}")

class PushNotificationService(NotificationService):
    def send_notification(self, message):
        print(f"Sending push notification: {message}")

class NotificationManager:
    def __init__(self, services):
        self.services = services

    def send_notification(self, message):
        for service in self.services:
            service.send_notification(message)

email_service = EmailService()
sms_service = SMSService()
push_notification_service = PushNotificationService()

notification_manager = NotificationManager([email_service, sms_service, push_notification_service])
notification_manager.send_notification("Hello, Kashishh")
