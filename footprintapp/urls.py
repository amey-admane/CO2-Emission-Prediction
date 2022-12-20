from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('home', views.foot_print,name= "home"),

    path('', views.foot_print,name= ""),
    path('cal', views.tresscal,name= "cal"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
