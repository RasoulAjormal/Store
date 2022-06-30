from django.db.models import Count, When, IntegerField, Case, Q
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from site_module.models import SiteBanner
from utils.convertors import group_list
from utils.http_service import get_client_ip
from .models import ProductModel, ProductCategoryModel, ProductBrandModel, ProductGalleryModel, ProductCommentModel, \
    ProductVisitModel


# Create your views here.
class ProductListView(ListView):
    template_name = 'product-List-View.html'
    model = ProductModel
    paginate_by = 9

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        request: HttpRequest = self.request
        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')
        if start_price is not None:
            query = query.filter(price__gte=start_price)
        if end_price is not None:
            query = query.filter(price__lte=end_price)
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        query = ProductModel.objects.filter(is_active=True)
        product: ProductModel = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 0
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or db_max_price
        context['products'] = ProductModel.objects.filter(is_active=True, is_delete=False)
        context['categories'] = ProductCategoryModel.objects.filter(is_active=True, is_delete=False)
        context['banners'] = SiteBanner.objects.filter(is_active=True,
                                                       position__iexact=SiteBanner.SiteBannerPositions.ProductListPageUrl)
        return context


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'Product-detail-View.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        context['banners'] = SiteBanner.objects.filter(is_active=True,
                                                       position__iexact=SiteBanner.SiteBannerPositions.ProductDetailPageUrl)
        loaded_product = self.object
        galleries = list(ProductGalleryModel.objects.filter(product_id=loaded_product.id))
        context['product_galleries_group'] = group_list(galleries, 3)
        context['product_comments'] = ProductCommentModel.objects.filter(is_delete=False, is_read_admin=True,
                                                                         product_id=loaded_product.id).order_by(
            '-created_time')
        context['product_comments_count'] = ProductCommentModel.objects.filter(is_delete=False, is_read_admin=True,
                                                                               product_id=loaded_product.id).count()
        product_with_brand = list(ProductModel.objects.filter(is_delete=False, is_active=True,
                                                              brand_id=loaded_product.brand.id))
        context['products_with_brand'] = group_list(product_with_brand, 3)
        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        has_been_visited = ProductVisitModel.objects.filter(ip=user_ip, product_id=loaded_product.id).exists()
        if not has_been_visited:
            new_visit = ProductVisitModel(ip=user_ip, product_id=loaded_product.id, user_id=user_id)
            new_visit.save()
        return context


class ProductCategoriesView(ListView):
    template_name = 'product-List-View.html'
    model = ProductModel
    paginate_by = 6

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        queryset = super(ProductCategoriesView, self).get_queryset()
        request: HttpRequest = self.request
        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')
        if start_price is not None:
            queryset = queryset.filter(price__gte=start_price)
        if end_price is not None:
            queryset = queryset.filter(price__lte=end_price)
        if category_id is not None:
            queryset = queryset.filter(category=category_id, is_active=True, is_delete=False)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoriesView, self).get_context_data()
        query = ProductModel.objects.filter(is_active=True)
        product: ProductModel = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 0
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or db_max_price
        context['categories'] = ProductCategoryModel.objects.filter(is_active=True, is_delete=False)
        return context


class ProductBrandsView(ListView):
    template_name = 'product-List-View.html'
    model = ProductModel

    def get_queryset(self):
        brand_id = self.kwargs.get('brand_id')
        queryset = super(ProductBrandsView, self).get_queryset()
        request: HttpRequest = self.request
        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')
        if start_price is not None:
            queryset = queryset.filter(price__gte=start_price)
        if end_price is not None:
            queryset = queryset.filter(price__lte=end_price)
        if brand_id is not None:
            queryset = queryset.filter(brand=brand_id, is_active=True)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductBrandsView, self).get_context_data()
        query = ProductModel.objects.filter(is_active=True)
        product: ProductModel = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 0
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or db_max_price
        return context


def add_comment_product(request: HttpRequest):
    if request.user.is_authenticated:
        ProductId = request.GET.get('productId')
        Full_Name = request.GET.get('full_name')
        Email = request.GET.get('email')
        Text = request.GET.get('text')
        if Full_Name != '' and Email != '' and Text != '':
            new_comment = ProductCommentModel(product_id=ProductId, user_id=request.user.id, text=Text, email=Email,
                                              full_name=Full_Name)
            new_comment.save()
            context = {
                'object': ProductModel.objects.filter(is_active=True, is_delete=False, id=ProductId).first(),
                'product_comments': ProductCommentModel.objects.filter(is_delete=False, is_read_admin=True,
                                                                       product_id=ProductId).order_by('-created_time'),
                'product_comments_count': ProductCommentModel.objects.filter(is_delete=False, is_read_admin=True,
                                                                             product_id=ProductId).count()
            }
            return render(request, 'include/product_comments_partial.html', context)
        else:
            return JsonResponse({'status': 'Invalid'})
    return JsonResponse({'status': 'PageLogin'})


def product_categories_component(request: HttpRequest):
    product_main_categories = ProductCategoryModel.objects.annotate(
        category_count=Count('productmodel')).prefetch_related(
        'productmodel_set').filter(is_active=True)
    return render(request, 'components/product_categories_component.html', {'main_categories': product_main_categories})


def product_brand_component(request: HttpRequest):
    brands = ProductBrandModel.objects.annotate(
        brand_count=Count('productmodel',
                          filter=Q(productmodel__is_active=True, productmodel__is_delete=False))).filter(is_active=True)
    return render(request, 'components/product_brand_component.html', {'brands': brands})
