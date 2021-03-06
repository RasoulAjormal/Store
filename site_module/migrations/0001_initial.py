# Generated by Django 3.1.14 on 2022-04-15 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLinkBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'دسته بندی لینک های فوتر',
                'verbose_name_plural': 'دسته یندی لینک های فوتر',
            },
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=50, verbose_name='نام سایت')),
                ('site_url', models.CharField(max_length=50, verbose_name='دامنه سایت')),
                ('address', models.CharField(max_length=300, verbose_name='آدرس')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='موبایل')),
                ('fax', models.CharField(blank=True, max_length=200, null=True, verbose_name='فکس')),
                ('email', models.CharField(max_length=200, verbose_name='ایمیل سایت')),
                ('copy_right', models.TextField(verbose_name='متن کپی رایت')),
                ('about_us_text', models.TextField(verbose_name='متن درباره ما')),
                ('site_logo', models.ImageField(upload_to='images', verbose_name='عکس سایت')),
                ('is_main_setting', models.BooleanField(verbose_name='تنظیمات سایت')),
            ],
            options={
                'verbose_name': 'تنظیم سایت',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url_title', models.CharField(max_length=200, verbose_name='عنوان لینک')),
                ('url', models.URLField(verbose_name='لینک')),
                ('description', models.TextField(verbose_name='توضیحات اسلایدر')),
                ('image', models.ImageField(upload_to='images/slaiders', verbose_name='تصویر اسلایدر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر ها',
            },
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url', models.URLField(max_length=500, verbose_name='لینک')),
                ('footer_link_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_module.footerlinkbox', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'لینک فوتر',
                'verbose_name_plural': 'لینک های فوتر',
            },
        ),
    ]
