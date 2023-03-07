from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from django_celery import settings


@shared_task(bind=True)
def test_func(self):
    for val in range(10):
        print(val)
    return "Done"

@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    print("===user", users)
    for user in users:
        mail_subject = "Hi this is for testing "
        message = "If you are liking my contect please click on below link"
        to_email = user.email
        print("===tomail", to_email)
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False

        )
    return "sent mail outside the django server"