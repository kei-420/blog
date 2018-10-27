from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import SignUpForm, LogInForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'accounts/signup.html', {'form': form})
        user_info_save = form.save(commit=True)

        auth_login(request, user_info_save)
        return redirect('accounts:login')


class LogInView(View):
    def get(self, request, *args, **kwargs):
        form = LogInForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LogInForm(request.POST)
        if not form.is_valid():
            return render(request, 'accounts/login.html', {'form': form})

        # -> get_user() > ユーザ名、データベースIDなどを表す引数 user_id をとり、対応するUserオブジェクトを返す。
        login_user = form.get_login_user()
        auth_login(request, login_user)

        return redirect(reverse('blog_app:home'))


class LogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            auth_logout(request)

        return redirect(reverse('accounts:login'))