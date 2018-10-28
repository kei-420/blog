from django.shortcuts import render, redirect, reverse
from django.views import View, generic
from .models import Post
from accounts.models import UserManager
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login as auth_login
from .forms import PostForm

from django.urls import reverse_lazy


class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        show_data = Post.objects.filter(user=request.user).order_by('-created_at')
        context = {
            'show_data': show_data,
        }
        return render(request, 'blog_app/home.html', context)


class PostView(LoginRequiredMixin, generic.FormView):
    template_name = 'blog_app/post.html'
    form_class = PostForm
    success_url = reverse_lazy('blog_app:home')

    def get_form_kwargs(self):
        kwargs = super(PostView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    # def get(self,request, *args, **kwargs):
    #     form = PostForm
    #     return render(request, 'blog_app/post.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, user=request.user)
        if not form.is_valid():
            return render(request, 'blog_app/post.html', {'form': form})

        form.save(commit=True)

        return redirect(reverse('blog_app:home'))
