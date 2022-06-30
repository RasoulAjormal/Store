from django.contrib import admin

# Register your models here.
from site_module.models import Slider, SiteSetting, FooterLinkBox, FooterLink, SiteBanner


class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'footer_link_box', 'url']
    list_editable = ['footer_link_box', 'url']


admin.site.register(Slider)
admin.site.register(SiteSetting)
admin.site.register(FooterLinkBox)
admin.site.register(FooterLink, FooterLinkAdmin)
admin.site.register(SiteBanner)
