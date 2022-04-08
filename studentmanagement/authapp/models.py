from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from rest_framework.response import Response


class User(AbstractUser):
    first_name = models.CharField(max_length=100, default="")
    middle_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    is_admin = models.BooleanField('admin status', default=False)
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
    


class StudentProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = f" Open the given below url and do the post request by passing two fields \n one as token and other as password \n in token pass the token given below and in password field write your new password \n http://127.0.0.1:8000{reverse('password_reset:reset-password-request')}confirm/ \n\n token : {reset_password_token.key}"
    send_mail(
        # title:
        "Mail to Reset Password",
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs,):
    if created and instance.is_student == True:
        StudentProfile.objects.create(user=instance)
