from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name="Home"),
    path('api/blooddonor', BloodDonorRegisterApiView.as_view(),
         name="BloodDonorRegisterApiView"),
    path("api/blooddonor/<int:pk>/", BloodDonorRegisterApiView.as_view(),
         name="BloodDonorRegisterApiViewview"),
]
