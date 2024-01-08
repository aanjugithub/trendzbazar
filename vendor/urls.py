from django.urls import path
from vendor import views
from rest_framework.routers import DefaultRouter




urlpatterns=[
    path('login/',views.LoginView.as_view())
    
] 

