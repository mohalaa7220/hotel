
from django.core.mail import send_mail
from django.conf import settings
settings.DEFAULT_FROM_EMAIL,


def email_send(name, email):
    send_mail(
        'Booking for Hotel',
        f'Hallo dear, {name} your booking is recived we will call you as soon as',
        'from@example.com',
        [email],
        fail_silently=False,
    )
