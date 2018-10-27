from django.urls import path
from . import views


app_name = 'blog_app'

urlpatterns = [
    # path('blog_name_create/', views.BlogNameCreateView.as_view(), name='blog_name'),
    path('home/', views.HomeView.as_view(), name='home'),
]