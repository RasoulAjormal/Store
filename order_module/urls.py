from django.urls import path

from order_module.views import OrderView, ChangeOrderDetailCount, DeleteOrderDetail, AddProductToOrder

urlpatterns = [
    path('', OrderView.as_view(), name='OrderUserBasketPageUrl'),
    path('change-detail-count', ChangeOrderDetailCount.as_view(), name='ChangeOrderDetailCount'),
    path('delete-order-detail', DeleteOrderDetail.as_view(), name='DeleteOrderDetail'),
    path('add-product-to-order', AddProductToOrder.as_view(), name='AddProductToOrder'),
]
