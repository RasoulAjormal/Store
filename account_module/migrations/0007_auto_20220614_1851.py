# Generated by Django 3.1.14 on 2022-06-14 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0006_user_about_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about_us',
            field=models.TextField(max_length=500, verbose_name='درباره من'),
        ),
    ]
