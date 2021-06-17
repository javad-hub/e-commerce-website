from django.urls import path
from .views import IndexPageView, ShopPageView

urlpatterns = [
    path('',IndexPageView.as_view(), name="index"),
    path('shop/',ShopPageView.as_view(), name="shop"),
]