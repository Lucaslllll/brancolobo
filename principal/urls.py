from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name="index"),
   
   path('add_doubt', views.add_doubt, name="add_doubt"),
   path('edit_doubt/<int:pk>', views.edit_doubt, name="edit_doubt"),
   path('list_doubt', views.list_doubt, name="list_doubt"),
   path('delete_doubt/<int:pk>', views.delete_doubt, name="delete_doubt"),

   path('add_client', views.add_client, name="add_client"),
   path('edit_client/<int:pk>', views.edit_client, name="edit_client"),
   path('list_client', views.list_client, name="list_client"),
   path('delete_client/<int:pk>', views.delete_client, name="delete_client"),
   
   path('login', views.do_login, name="login"),
   path('forget_password', views.forget_password, name='forget_password'),
   
]