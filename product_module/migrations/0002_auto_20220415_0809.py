# Generated by Django 3.1.14 on 2022-04-15 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=10, verbose_name='قیمت'),
        ),
    ]
