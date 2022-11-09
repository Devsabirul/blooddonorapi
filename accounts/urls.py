from django.urls import path
from .views import *
urlpatterns = [
    path('/accounts', AccountsApi.as_view(), name="account api"),
    path('/accounts/<int:pk>', AccountsApi.as_view(),
         name="account api Get by id"),
    path('/account/register', UserRegistrationView.as_view(),
         name="Registration api"),
    path('/account/login', UserLoginApiView.as_view(), name="loginapi")
]
