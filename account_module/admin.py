from django.contrib import admin

# Register your models here.
from account_module import models

admin.site.register(models.User)
