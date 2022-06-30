from django.urls import path

from home_module.views import HomeView, AboutView,add_email_to_send_news

urlpatterns = [
    path('', HomeView.as_view(), name='HomePageUrl'),
    path('about/', AboutView.as_view(), name='AboutPageUrl'),
    path('add-email-to-send-news', add_email_to_send_news, name='AddEmailToSendNews'),

]
