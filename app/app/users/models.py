from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):

    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(
        _("Name of User"), blank=True, max_length=255
    )
    telephone = PhoneNumberField("Telephone", blank=True)
    notes = models.TextField("Notes", blank=True)

    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.username}
        )
