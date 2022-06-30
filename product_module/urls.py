from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCategoriesView, ProductBrandsView, add_comment_product

urlpatterns = [
    path('', ProductListView.as_view(), name='ProductListPageUrl'),
    path('cat/<category_id>', ProductCategoriesView.as_view(), name='ProductCategoryPageUrl'),
    path('brand/<brand_id>', ProductBrandsView.as_view(), name='ProductBrandsPageUrl'),
    path('<slug:slug>', ProductDetailView.as_view(), name='ProductDetailPageUrl'),
    path('add-comment-product/', add_comment_product, name='AddCommentProductPageUrl'),
]
