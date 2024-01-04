from django.contrib import admin
from .models import Customer, Product, Orders, Feedback, Cart, Wishlist, Like
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class CartAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cart, CartAdmin)


class WishlistAdmin(admin.ModelAdmin):
    pass


admin.site.register(Wishlist, WishlistAdmin)


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Orders, OrderAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    pass


admin.site.register(Feedback, FeedbackAdmin)


class LikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Like, LikeAdmin)
# Register your models here.
