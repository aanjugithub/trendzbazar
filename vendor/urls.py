from django.urls import path
from vendor import views


urlpatterns = [
   
    
    path('login/',views.LogInView.as_view(),name="signin"),
    path('register/',views.RegistartionView.as_view(),name="register"),
    
] 