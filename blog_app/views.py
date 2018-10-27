from django.shortcuts import render, redirect
from django.views import View
from .models import Post, Blog
from accounts.models import UserManager
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login as auth_login


class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.order_by('-created_at')
        return render(request, 'blog_app/home.html', {'post': post})
