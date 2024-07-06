from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about-us', views.About),
    path('login', views.login),
    path('serch', views.Serch),
    path('Reg', views.Reg),
    path('account', views.account),
    path('index', views.index)
]
