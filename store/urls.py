from django.urls import path
from .views import (IndexPageView, ShopPageView, AboutPageView, CartPageView, CheckOutPageView, ContactPageView, AccountPageView, ServicePageView,
    ShopDetailPageView, WishListlPageView)

urlpatterns = [
    path('',IndexPageView.as_view(), name="index"),
    path('shop/',ShopPageView.as_view(), name="shop"),
    path('about/',AboutPageView.as_view(), name="about"),
    path('cart/',CartPageView.as_view(), name="cart"),
    path('checkout/',CheckOutPageView.as_view(), name="checkout"),
    path('contact-us/',ContactPageView.as_view(), name="contact"),
    path('your-account/',AccountPageView.as_view(), name="my_account"),
    path('services/',ServicePageView.as_view(), name="service"),
    path('shop-detail/',ShopDetailPageView.as_view(), name="shop-detail"),
    path('wishlist/',WishListlPageView.as_view(), name="wishlist"),
]