from django.urls import path
from .api_views import PostListCreateAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='api-posts'),
]
