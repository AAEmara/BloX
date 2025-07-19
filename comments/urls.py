from django.urls import path
from .views import PostCommentsAPIView

urlpatterns = [
    path('api/posts/<int:pk>/comments/',PostCommentsAPIView.as_view(),name='api_post_comments')
]