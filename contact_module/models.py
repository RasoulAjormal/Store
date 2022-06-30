from django.db import models


# Create your models here.
class ContactUsModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    email = models.EmailField(verbose_name='ایمیل')
    fullname = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    message = models.TextField(max_length=500, verbose_name='پیغام')
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خوانده شد / نشده')
    created_data = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)

    class Meta:
        verbose_name = 'پیغام'
        verbose_name_plural = 'پیغام ها'

    def __str__(self):
        return self.title


class SendNewsModel(models.Model):
    email = models.EmailField(max_length=200, verbose_name='ایمیل', unique=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'ایمیل'
        verbose_name_plural = 'ایمیل ها'
