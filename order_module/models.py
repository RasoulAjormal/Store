from django.db import models

# Create your models here.
from account_module.models import User
from product_module.models import ProductModel


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(default=False, verbose_name='نهایی شده/نشده')
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    def calculate_total_price(self):
        total_amount = 0
        if self.is_paid:
            for order_detail in self.orderdetail_set.all():
                if order_detail.count < 1:
                    order_detail.count = 1
                    order_detail.save()
                total_amount += order_detail.final_price * order_detail.count
            return total_amount
        for order_detail in self.orderdetail_set.all():
            if order_detail.count < 1:
                order_detail.count = 1
                order_detail.save()
            total_amount += order_detail.product.price * order_detail.count
        return total_amount

    def __str__(self):
        return self.user.__str__()

    class Meta:
        verbose_name = 'سبد خرید کاربر'
        verbose_name_plural = 'سبد های خرید کاربر'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def get_total_price(self):
        return self.count * self.product.price

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'جزئیات سبد خرید'
        verbose_name_plural = 'لیست جزئیات سبد خرید'
