# Generated by Django 3.1.14 on 2022-06-18 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0004_auto_20220616_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitebanner',
            name='position',
            field=models.CharField(choices=[('ProductListPageUrl', 'صفحه لیست محصولات'), ('ProductDetailPageUrl', 'صفحه جزئیات محصولات'), ('ArticlesPageUrl', 'لیست مقالات'), ('ArticleDetail', 'جزئیات مقالات'), ('AboutPageUrl', 'درباره ما')], max_length=200),
        ),
    ]
