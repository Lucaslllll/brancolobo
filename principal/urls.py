from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('login', views.do_login, name="login"),
   path('forget_password', views.forget_password, name='forget_password'),
   
]