from django.contrib import admin
from .models import ProductModel, ProductBrandModel, ProductTagModel, ProductCategoryModel, ProductGalleryModel, ProductCommentModel

# Register your models here.

admin.site.register(ProductModel)
admin.site.register(ProductBrandModel)
admin.site.register(ProductTagModel)
admin.site.register(ProductCategoryModel)
admin.site.register(ProductGalleryModel)
admin.site.register(ProductCommentModel)
