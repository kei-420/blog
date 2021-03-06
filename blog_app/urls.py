from django.urls import path
from . import views


app_name = 'blog_app'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/post', views.PostView.as_view(), name='post'),
    path('home/post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
]