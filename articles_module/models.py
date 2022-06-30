from django.contrib.auth.decorators import login_required
from django.db import models

# Create your models here.
from account_module.models import User


class ArticleCategoryModel(models.Model):
    parent = models.ForeignKey('ArticleCategoryModel', null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name='دسته بندی والد')
    title = models.CharField(max_length=50, verbose_name='عنوان')
    url_title = models.CharField(max_length=100, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی های مقاله'


class ArticleModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True, verbose_name='عنوان در url')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', editable=False, null=True)
    CreatedTime = models.TimeField(auto_now_add=True, verbose_name='ساعت ایجاد مقاله')
    CreatedDate = models.DateField(auto_now_add=True, verbose_name='تاریخ ایجاد مقاله')
    image = models.ImageField(upload_to='images/articles/', verbose_name='تصویر مقاله')
    description = models.TextField(verbose_name='توضحات مقاله')
    article_category = models.ManyToManyField(ArticleCategoryModel, null=True, blank=True,
                                              verbose_name='دسته بندی محصول')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='پاک شده / پاک نشده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class ArticleCommentModel(models.Model):
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE, verbose_name='مقاله', null=True)
    parent = models.ForeignKey('ArticleCommentModel', null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name='پیغام والد')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    full_name = models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')
    createdTime = models.TimeField(auto_now_add=True, verbose_name='ساعت ایجاد مقاله')
    createdDate = models.DateField(auto_now_add=True, verbose_name='تاریخ ایجاد مقاله')
    message = models.TextField(max_length=500, verbose_name='پیغام')
    is_read_admin = models.BooleanField(default=False, verbose_name='خوانده شده/نشده توسط ادمین')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/نشده')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'پیغام'
        verbose_name_plural = 'پیغام ها'
