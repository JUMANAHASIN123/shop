from django.urls import path
from .import views

urlpatterns=[
    path('customerhome',views.customer_home)
]