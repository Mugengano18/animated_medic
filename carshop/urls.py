from django.urls import path
from carshop import views

urlpatterns = [
    path("", views.home, name="home"),
    path("shop_register/",views.shop_register, name="shop"),
]