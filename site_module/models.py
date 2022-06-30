from django.db import models


# Create your models here.
class SiteSetting(models.Model):
    site_name = models.CharField(max_length=50, verbose_name='نام سایت')
    site_url = models.CharField(max_length=50, verbose_name='دامنه سایت')
    address = models.CharField(max_length=300, verbose_name='آدرس')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='موبایل')
    fax = models.CharField(max_length=200, null=True, blank=True, verbose_name='فکس')
    email = models.CharField(max_length=200, verbose_name='ایمیل سایت')
    copy_right = models.TextField(verbose_name='متن کپی رایت')
    about_us_text = models.TextField(verbose_name='متن درباره ما')
    site_logo = models.ImageField(upload_to='images/logo', verbose_name='عکس سایت')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات سایت')

    class Meta:
        verbose_name = 'تنظیم سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return self.site_name


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url_title = models.CharField(max_length=200, verbose_name='عنوان لینک')
    url = models.URLField(max_length=200, verbose_name='لینک')
    description = models.TextField(verbose_name='توضیحات اسلایدر')
    image = models.ImageField(upload_to='images/slaiders', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title


class SiteBanner(models.Model):
    class SiteBannerPositions(models.TextChoices):
        ProductListPageUrl = 'ProductListPageUrl', 'صفحه لیست محصولات'
        ProductDetailPageUrl = 'ProductDetailPageUrl', 'صفحه جزئیات محصولات'
        ArticlesPageUrl = 'ArticlesPageUrl', 'لیست مقالات'
        ArticleDetail = 'ArticleDetail', 'جزئیات مقالات'
        AboutPageUrl = 'AboutPageUrl', 'درباره ما'

    title = models.CharField(max_length=50, verbose_name='عنوان بنر')
    url = models.URLField(max_length=600, verbose_name='آدرس بنر')
    image = models.ImageField(upload_to='images/SiteBanner/', verbose_name='تصویر بنر')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')
    position = models.CharField(max_length=200, choices=SiteBannerPositions.choices)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بنر سایت'
        verbose_name_plural = 'بنر های سایت'


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته یندی لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title
