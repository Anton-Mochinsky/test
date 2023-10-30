from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from jk.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=255, unique=True)
    email = models.EmailField(_('email address'),\
        null=True, blank=True)
    phone = models.CharField(_('phone number'), max_length=30,\
        null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)

    is_verified = models.BooleanField(_('verified'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        unique_together = ('username', 'email', 'phone')


class MeterReading(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"))
    date = models.DateTimeField(_('reading date'), auto_now_add=True)
    hot_water_reading = models.DecimalField(_('hot water reading'), max_digits=10, decimal_places=3)
    cold_water_reading = models.DecimalField(_('cold water reading'), max_digits=10, decimal_places=3)
    gas_reading = models.DecimalField(_('gas reading'), max_digits=10, decimal_places=3)
    electricity_reading = models.DecimalField(_('electricity reading'), max_digits=10, decimal_places=3)

    class Meta:
        verbose_name = _('meter reading')
        verbose_name_plural = _('meter readings')
