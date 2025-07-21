from django.urls import path
from .views import register_view, login_view, logout_view

app_name = 'blog_auth' # This is crucial and correctly defined

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
