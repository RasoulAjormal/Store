# Generated by Django 3.1.14 on 2022-06-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0008_auto_20220614_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
    ]
