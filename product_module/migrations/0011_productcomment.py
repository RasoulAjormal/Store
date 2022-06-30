# Generated by Django 3.1.14 on 2022-06-17 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product_module', '0010_auto_20220616_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='ساعت ایجاد نظر')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='تاریخ ایجاد نظر')),
                ('text', models.TextField(max_length=700, verbose_name='متن نظر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='محصول')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'نظر محصول',
                'verbose_name_plural': 'نظرات محصولات',
            },
        ),
    ]
