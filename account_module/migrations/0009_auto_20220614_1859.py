# Generated by Django 3.1.14 on 2022-06-14 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0008_auto_20220614_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/user/', verbose_name='تصویر کاربر'),
        ),
    ]
