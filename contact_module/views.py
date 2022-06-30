import geocoder
from django.views.generic import CreateView
from folium import folium, Marker

from contact_module.forms import ContactUsForm
# Create your views here.
from site_module.models import SiteSetting


class ContactUsView(CreateView):
    template_name = 'contact-us-page.html'
    form_class = ContactUsForm
    success_url = '/ContactUs'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super(ContactUsView, self).get_context_data()
        context['SiteSetting'] = SiteSetting.objects.filter(is_main_setting=True).first()
        location = geocoder.osm('شوشتر دانشگاه آزاد')
        lat = location.lat
        lng = location.lng
        country = location.country
        m = folium.Map(location=[lat, lng], zoom_start=15)
        Marker([lat, lng], tooltip='We are here', popup=country).add_to(m)
        context['map'] = m._repr_html_()
        return context
