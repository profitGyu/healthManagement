from django.contrib.auth.views import LogoutView
from django.urls import path
from user.views import hello, Index, UserRegistrationView, UserLoginView

urlpatterns = [
    path('hello/<to>', hello),
    path('create/', UserRegistrationView.as_view(), name="create_user"),
    path('login/', UserLoginView.as_view(), name="login_user"),
    path('logout/', LogoutView.as_view(), name="logout_user"),
]