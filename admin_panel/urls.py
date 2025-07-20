from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('admins/', views.user_list, name='user_list'),
  
]