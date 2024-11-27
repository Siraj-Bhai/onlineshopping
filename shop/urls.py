from django.urls import path
from pkg_resources.extern import names

from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("register",views.register,name="register"),
    path("collections",views.collections,name="collections"),
    path("collections/<str:name>",views.collectionsview,name="collections"),
    path("collections/<str:cname>/<str:pname>",views.productdetails,name="productdetails")
]