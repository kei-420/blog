from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('confirm_register_information', views.ConfirmUserInfo.as_view(), name='confirm_user_info'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]