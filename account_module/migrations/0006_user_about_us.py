# Generated by Django 3.1.14 on 2022-06-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0005_auto_20220417_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_us',
            field=models.TextField(max_length=500, null=True, verbose_name='درباره من'),
        ),
    ]
