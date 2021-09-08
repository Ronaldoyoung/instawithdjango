from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.template.loader import render_to_string

# Create your models here.

class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성"
        FEMALE = "F", "여성"

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13, blank=True, validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")])
    gender = models.CharField(max_length=1, blank=True, choices=GenderChoices.choices)

    def send_welcome_email(self):

        subject = render_to_string("accounts/welcome_email_subject.txt", {
            "user": self,
        })
        content = render_to_string("accounts/welcome_email_content.txt", {
            "user": self,
        })
        sender_email = settings.WELCOME_EMAIL_SENDER
        send_mail(subject=subject, message=content, from_email=sender_email, recipient_list=[self.email], fail_silently=False)