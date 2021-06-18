from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'index.html'

class ShopPageView(TemplateView):
    template_name = 'shop.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class CartPageView(TemplateView):
    template_name = 'cart.html'

class CheckOutPageView(TemplateView):
    template_name = 'checkout.html'

class ContactPageView(TemplateView):
    template_name = 'contact-us.html'

class AccountPageView(TemplateView):
    template_name = 'my-account.html'

class ServicePageView(TemplateView):
    template_name = 'service.html'

class ShopDetailPageView(TemplateView):
    template_name = 'shop-detail.html'

class WishListlPageView(TemplateView):
    template_name = 'wishlist.html'