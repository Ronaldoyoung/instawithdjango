from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.conf import settings
from django.db import models
from django.template.loader import render_to_string

# Create your models here.


class User(AbstractUser):
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)

    def send_welcome_email(self):

        subject = render_to_string("accounts/welcome_email_subject.txt", {
            "user": self,
        })
        content = render_to_string("accounts/welcome_email_content.txt", {
            "user": self,
        })
        sender_email = settings.WELCOME_EMAIL_SENDER
        send_mail(subject=subject, message=content, from_email=sender_email, recipient_list=[self.email], fail_silently=False)

    # def save(self, *args, **kwargs):
    #     is_created = (self.pk == None)
    #     super().save(*args, **kwargs)
    #
    #     if is_created: