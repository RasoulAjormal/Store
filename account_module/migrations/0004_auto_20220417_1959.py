# Generated by Django 3.1.14 on 2022-04-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0003_singinmodel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singinmodel',
            name='username',
            field=models.CharField(max_length=50, verbose_name='نام کاربری'),
        ),
    ]
