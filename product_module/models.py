from django.db import models
# Create your models here.
from django.urls import reverse
from django.utils.text import slugify

from account_module.models import User


class ProductBrandModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='نام برند')
    is_active = models.BooleanField(verbose_name='فعال/غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'


class ProductCategoryModel(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/نشده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductTagModel(models.Model):
    caption = models.CharField(max_length=50, verbose_name='عنوان')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


class ProductModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='نام کالا')
    brand = models.ForeignKey(ProductBrandModel, on_delete=models.CASCADE, null=True, blank=True, verbose_name='برند')
    category = models.ForeignKey(ProductCategoryModel, on_delete=models.CASCADE, null=True, verbose_name='دسته بندی ها')
    tag = models.ForeignKey(ProductTagModel, null=True, blank=True, on_delete=models.CASCADE, verbose_name='تگ ها')
    price = models.IntegerField(verbose_name='قیمت')
    number = models.IntegerField(verbose_name='تعداد', null=True, blank=False)
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='عکس')
    short_description = models.TextField(verbose_name='توضیح کوتاه')
    description = models.TextField(verbose_name='توضیحات محصول')
    slug = models.SlugField(max_length=200, default='', null=False, blank=True, unique=True,
                            verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/نشده')

    def get_absolute_url(self):
        return reverse('ProductDetailPageUrl', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductGalleryModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to='images/ProductGallery', verbose_name='تصویر')

    class Meta:
        verbose_name = 'تصویر گالری'
        verbose_name_plural = 'گالری تصاویر'

    def __str__(self):
        return self.product.title


class ProductCommentModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='محصول')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    full_name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی', null=True)
    email = models.EmailField(max_length=100, verbose_name='ایمیل', null=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='ساعت ایجاد نظر')
    created_date = models.DateField(auto_now_add=True, verbose_name='تاریخ ایجاد نظر')
    text = models.TextField(max_length=700, verbose_name='متن نظر')
    is_read_admin = models.BooleanField(default=True, verbose_name='خوانده شده/نشده توسط ادمین')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/نشده')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'نظر محصول'
        verbose_name_plural = 'نظرات محصولات'


class ProductVisitModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='محصول')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', null=True, blank=True)
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')

    def __str__(self):
        return f'{self.product.title} / {self.ip}'

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدید های محصول'
