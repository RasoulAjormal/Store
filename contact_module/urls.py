from django.urls import path
from contact_module.views import ContactUsView

urlpatterns = [
    path('', ContactUsView.as_view(), name='ContactUsPageUrl'),
]
