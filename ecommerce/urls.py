
from django.contrib import admin
from django.urls import path
from django.conf import settings
from ecom import views
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name=''),
    path('wishlist', views.wishlist, name=''),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('logout', views.logout, name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view, name='contactus'),
    path('search', views.search_view, name='search'),
    path('send-feedback', views.send_feedback_view, name='send-feedback'),
    path('view-feedback', views.view_feedback_view, name='view-feedback'),
    path('productdetail/<int:pk>', views.product_detail, name='add-to-cart'),
    path('addreview/<str:pk>', views.addreview, name='addreview'),
    path('helpful/<str:kl>/<str:pk>', views.helpful, name='helpful'),

    path('adminclick', views.adminclick_view), path('productcategory', views.productcategory), path(
        'hightolow/<str:id>', views.hightolow), path(
        'lowtohigh/<str:id>', views.lowtohigh),
    path('adminlogin', LoginView.as_view(
        template_name='ecom/adminlogin.html'), name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),

    path('view-customer', views.view_customer_view, name='view-customer'),
    path('productmen', views.productmen, name='productmen'),
    path('productwomen', views.productwomen, name='productwomen'),
    path('delete-customer/<int:pk>',
         views.delete_customer_view, name='delete-customer'),
    path('update-customer/<int:pk>',
         views.update_customer_view, name='update-customer'),

    path('admin-products', views.admin_products_view, name='admin-products'),
    path('admin-add-product', views.admin_add_product_view,
         name='admin-add-product'),
    path('delete-product/<int:pk>',
         views.delete_product_view, name='delete-product'),
    path('update-product/<int:pk>',
         views.update_product_view, name='update-product'),
    path('loginuser', views.loginuser, name='loginuser'),
    path('admin-view-booking', views.admin_view_booking_view,
         name='admin-view-booking'),
    path('delete-order/<int:pk>', views.delete_order_view, name='delete-order'),
    path('update-order/<int:pk>', views.update_order_view, name='update-order'),
    path('signup', views.signup, name="signup"),
    path('quick', views.gh, name="gh"),
    path('between', views.between, name="beetween"),
    path('customersignup', views.customer_signup_view),
    path('customerlogin', LoginView.as_view(
        template_name='website/login.html'), name='customerlogin'),
    path('customer-home', views.customer_home_view, name='customer-home'),
    path('my-order', views.my_order_view, name='my-order'),
    path('checkout', views.checkout, name='checkout'),
    path('profile', views.my_profile_view, name='my-profile'),
    path('edit-profile', views.edit_profile_view, name='edit-profile'),
    path('download-invoice/<int:orderID>/<int:productID>',
         views.download_invoice_view, name='download-invoice'),
    path("products", views.products, name="products"),
    path("producttshirt", views.producttshirt, name="producttshirt"),
    path("producthoodie", views.producthoodie, name="producthoodie"),
    path("productkeychain", views.productkeychain, name="productkeychain"),
    path("productbracelet", views.productbracelet, name="productbracelet"),

    path("productartistic", views.productartistic, name="productartistic"), path(
        "productcap", views.productcap, name="productcap"),
    path("order", views.order, name="order"),
    path("invoice/<str:pk>", views.invoice, name="invoice"),
    path("verify/<str:auth_token>", views.verify, name="verify"),
    path("cancel/<str:pk>", views.cancel, name="cancel"),

    path('add-to-cart/<int:pk>', views.add_to_cart_view, name='add-to-cart'),
    path('add-to-wishlist/<int:pk>', views.add_to_wishlist, name='add-to-wishlist'),
    path('delete/<int:id>', views.deletecart, name='deletecart'),
    path('removeone/<int:pk>', views.remove_one, name='remove_one'),
    path('cart', views.cart_view, name='cart'),
    path('remove-from-cart/<int:pk>',
         views.remove_from_cart_view, name='remove-from-cart'),
    path('customer-address', views.customer_address_view, name='customer-address'),
    path('payment-success', views.payment_success_view, name='payment-success'),
    #     path("search", views.search, name="search")

]
urlpatterns += static(settings.MEDIA_ROOT)
