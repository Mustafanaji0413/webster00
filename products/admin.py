from django.contrib import admin
from .models import Product, Category, ReviewRating, Wishlist


# Product admin fields


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'category',
        'name',
        'price',
        'rating',
        'image',
        'wheight',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ReviewRating)
admin.site.register(Wishlist)