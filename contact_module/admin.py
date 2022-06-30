from django.contrib import admin

# Register your models here.
from contact_module.models import ContactUsModel, SendNewsModel


class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'title', 'is_read_by_admin']


admin.site.register(SendNewsModel)
admin.site.register(ContactUsModel, ContactUsModelAdmin)
