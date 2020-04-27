from django.template.loader import render_to_string
from smtplib import SMTPAuthenticationError
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail


def send_contact_mail(request):
    """
    this function send subscribtion to you email with order
    """
    data = request.POST
    try:
        send_mail(
            'New message from ["email"]'
            f"You have new message: {data['message']}\nFrom: {data['name']}",
            settings.FROM_EMAIL,
            ["mattbassdeveloper@gmail.com"],
            fail_silently=False,
        )
    except SMTPAuthenticationError:
        messages.error(request, "Your order confirmation email send failed")


def send_subscribe_mail(data):
    """
    this function send subscribtion to you email with order
    """

    html_message = render_to_string(
        "subscribe_mail.html", {"mail": data["email"]}
    )
    send_mail(
        "You will be updated about our new products and promotions.",
        settings.FROM_EMAIL,
        [data["email"]],
        fail_silently=False,
        html_message=html_message,
    )
