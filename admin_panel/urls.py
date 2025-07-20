from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('admins/', views.user_list, name='user_list'),
    path('admins/block/<int:user_id>/', views.block_user, name='block_user'),
    path('admins/unblock/<int:user_id>/', views.unblock_user, name='unblock_user'),
]