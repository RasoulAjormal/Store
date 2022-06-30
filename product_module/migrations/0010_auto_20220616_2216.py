# Generated by Django 3.1.14 on 2022-06-16 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0009_auto_20220614_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/ProductGallery', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'تصویر گالری',
                'verbose_name_plural': 'گالری تصاویر',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='Images',
        ),
        migrations.DeleteModel(
            name='ProductImages',
        ),
        migrations.AddField(
            model_name='productgallery',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='محصول'),
        ),
    ]
