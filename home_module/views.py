import geocoder
from django.db.models import Count
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from folium import folium, Marker

from contact_module.forms import SendNewsForm
from contact_module.models import SendNewsModel
from product_module.models import ProductModel, ProductCategoryModel
from site_module.models import SiteSetting, FooterLinkBox, Slider
# Create your views here.
from utils.convertors import group_list


class HomeView(TemplateView):
    template_name = 'index_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['Sliders'] = Slider.objects.filter(is_active=True)[:12]
        groups_latest = ProductModel.objects.filter(is_active=True, is_delete=False).order_by('-id')[:12]
        context['new_products'] = group_list(groups_latest)
        groups_visit = list(ProductModel.objects.annotate(
            product_visit_number=Count('productvisitmodel')).prefetch_related('productvisitmodel_set').filter(
            is_delete=False, is_active=True).order_by('-product_visit_number')[:12])
        context['groups_latest'] = group_list(groups_latest)
        context['product_visited'] = group_list(groups_visit)
        groups_categories = list(
            ProductCategoryModel.objects.annotate(products_count=Count('productmodel')).filter(
                is_active=True,
                is_delete=False, products_count__gt=0).order_by('-id')[:12])

        context['product_category'] = group_list(groups_categories)
        categories_products = []
        for category in groups_categories:
            item = {
                'id': category.id,
                'title': category.title,
                'products': category.productmodel_set.all()[:4],
            }
            categories_products.append(item)
        context['categories_products'] = categories_products
        product_sellers = list(
            ProductModel.objects.filter(is_active=True, is_delete=False, orderdetail__order__is_paid=True).order_by(
                '-orderdetail__count'))[:12]
        context['product_sellers'] = group_list(product_sellers)

        return context


class AboutView(TemplateView):
    template_name = 'About.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data()
        context['SiteSetting'] = SiteSetting.objects.filter(is_main_setting=True).first()
        location = geocoder.osm('شوشتر دانشگاه آزاد')
        lat = location.lat
        lng = location.lng
        country = location.country
        m = folium.Map(location=[lat, lng], zoom_start=15)
        Marker([lat, lng], tooltip='We are here', popup=country).add_to(m)
        context['map'] = m._repr_html_()
        return context


def site_header_partial(request):
    Setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    return render(request, 'shared/site-header-partial.html', {'Setting': Setting})


def site_footer_partial(request):
    Setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    Footer_Link_Box = FooterLinkBox.objects.all()
    Email = SendNewsForm()
    return render(request, 'shared/site-footer-partial.html',
                  {'Setting': Setting, 'Footer_Link_Box': Footer_Link_Box, 'SendNews': Email})


def add_email_to_send_news(request: HttpRequest):
    SendNews = SendNewsForm(request.GET)
    email = request.GET.get('email')
    if SendNewsModel.objects.filter(email=email).exists():
        return JsonResponse({'status': 'Repetitious'})
    if SendNews.is_valid():
        new_email = SendNewsModel(email=email)
        new_email.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'Invalid'})
