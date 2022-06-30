from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/user/', verbose_name='تصویر کاربر', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعال سازی ایمیل')
    about_us = models.TextField(verbose_name='درباره من', null=True, blank=True)
    address = models.CharField(max_length=100, null=True, verbose_name='آدرس')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name != '' and self.last_name != '':
            return self.get_full_name()
        else:
            return self.email


class SingInModel(models.Model):
    username = models.CharField(max_length=50, verbose_name='نام کاربری')
    email = models.CharField(max_length=50, verbose_name='ایمیل')
    password = models.CharField(max_length=50, verbose_name='پسورد')
    confirm_password = models.CharField(max_length=50, verbose_name='تکرار پسورد')

    class Meta:
        verbose_name = 'حساب کاربری'
        verbose_name_plural = 'حساب کاربر ها'


class LogInModel(models.Model):
    username = models.CharField(max_length=50, verbose_name='نام کاربری')
    password = models.CharField(max_length=50, verbose_name='پسورد')
    checkbox = models.BooleanField(default=False)
