# Generated by Django 3.1.14 on 2022-06-17 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0014_auto_20220617_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcommentmodel',
            name='email',
            field=models.EmailField(max_length=100, null=True, verbose_name='ایمیل'),
        ),
        migrations.AddField(
            model_name='productcommentmodel',
            name='full_name',
            field=models.CharField(max_length=100, null=True, verbose_name='نام و نام خانوادگی'),
        ),
    ]
