from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<int:category_id>/subscribe/', views.subscribe_category, name='subscribe_category'),
    path('category/<int:category_id>/unsubscribe/', views.unsubscribe_category, name='unsubscribe_category'),
]
