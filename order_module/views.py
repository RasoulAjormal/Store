from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView

from order_module.models import Order, OrderDetail
from product_module.models import ProductModel


@method_decorator(login_required, name='dispatch')
class OrderView(ListView):
    template_name = 'user_basket.html'
    model = OrderDetail

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrderView, self).get_context_data()
        current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                                 user_id=self.request.user.id)
        context['sum'] = current_order.calculate_total_price()
        context['order_detail'] = current_order
        return context


class AddProductToOrder(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            product_id = int(self.request.GET.get('product_id'))
            product_count = int(self.request.GET.get('product_count'))
            if product_count < 1:
                return JsonResponse({
                    'status': 'invalid_count',
                    'text': 'مقدار وارد شده معتبر نمی باشد',
                    'confirmButtonText': 'مرسی از شما',
                    'icon': 'warning'
                })
            product = ProductModel.objects.filter(is_active=True, is_delete=False, id=product_id).first()
            if product is not None:
                current_order, crated = Order.objects.get_or_create(user_id=request.user.id, is_paid=False)
                current_order_detail = current_order.orderdetail_set.filter(product_id=product.id).first()
                if current_order_detail is not None:
                    current_order_detail.count += product_count
                    current_order_detail.save()
                else:
                    new_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=product_count)
                    new_detail.save()
                return JsonResponse({
                    'status': 'success',
                    'text': 'با موفقیت به سبد خرید شما اضافه شد.',
                    'confirmButtonText': 'ممنون',
                    'icon': 'success'
                })
            else:
                return JsonResponse({
                    'status': 'not_found',
                    'text': 'محصول مورد نظر یافت نشد',
                    'confirmButtonText': 'مرسییییی',
                    'icon': 'error'
                })

        else:
            return JsonResponse({
                'status': 'not_auth',
                'text': 'لطفاََ اول وارد شوید',
                'confirmButtonText': 'ورود به سایت',
                'icon': 'error'
            })


@method_decorator(login_required, name='dispatch')
class ChangeOrderDetailCount(View):
    def get(self, request: HttpRequest):
        detail_id = self.request.GET.get('detail_id')
        state = self.request.GET.get('state')
        if detail_id is None or state is None:
            return JsonResponse({
                'status': 'not_found_detail_or_state'
            })
        change_detail = OrderDetail.objects.prefetch_related().filter(order__is_paid=False, id=detail_id,
                                                                      order__user_id=request.user.id).first()
        if state == 'Increase':
            if change_detail.count == change_detail.product.number:
                change_detail.count = change_detail.product.number
                change_detail.save()
            else:
                change_detail.count += 1
                change_detail.save()
        else:
            if change_detail.count > 1:
                change_detail.count -= 1
                change_detail.save()
            else:
                change_detail.count = 1
                change_detail.save()
        current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                                 user_id=request.user.id)
        context = {
            'order_detail': current_order,
            'sum': current_order.calculate_total_price()
        }
        return JsonResponse({
            'status': 'success',
            'body': render_to_string('user_basket_content.html', context)
        })


@method_decorator(login_required, name='dispatch')
class DeleteOrderDetail(View):
    def get(self, request: HttpRequest):
        detail_id = self.request.GET.get('detail_id')
        if detail_id is None:
            return JsonResponse({
                'status': 'not_found_detail_id'
            })
        change_detail = OrderDetail.objects.prefetch_related().filter(order__is_paid=False, id=detail_id,
                                                                      order__user_id=request.user.id).first()
        change_detail.delete()
        current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                                 user_id=request.user.id)
        context = {
            'order_detail': current_order,
            'sum': current_order.calculate_total_price()
        }
        return JsonResponse({
            'status': 'success',
            'body': render_to_string('user_basket_content.html', context)
        })
