from django.urls import path
from . import views


urlpatterns = [
     path('api/hello/', views.get_my_ipaddress, name="Ip_address")
]
