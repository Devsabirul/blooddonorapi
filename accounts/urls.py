from django.urls import path
from .views import *
urlpatterns = [
    path('/accounts', RegisterApi.as_view(), name="Register api"),
    path('/accounts/<int:pk>', RegisterApi.as_view(),
         name="Register api Get by id")
]
