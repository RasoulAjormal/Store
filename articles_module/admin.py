from django.contrib import admin

# Register your models here.
from articles_module import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        return super(ArticleAdmin, self).save_model(request, obj, form, change)


admin.site.register(models.ArticleCategoryModel)
admin.site.register(models.ArticleCommentModel)
