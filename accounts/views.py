from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm
from django.contrib.auth import login as auth_login, logout as auth_logout


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'accounts/signup.html', {'form': form})
        user_info_saved = form.save(commit=True)

        auth_login(request, user_info_saved)
        return redirect('accounts:login')


class LogInView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/login.html')


