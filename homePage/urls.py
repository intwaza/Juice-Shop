from django.conf.urls import url
from django.urls import path
from .views import home, product_view, register, register_list, registered

urlpatterns=[
    path("", home, name="home_view"),
    path("profile/<int:id>/", product_view, name="product_view"),
    path("register", register, name="register"),
    path("list/", register_list, name="list"),
    path("registered", registered, name="registered")
]