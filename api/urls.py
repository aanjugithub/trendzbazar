from django.urls import path
from api import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("products",views.ProductView,basename="products")
router.register("baskets",views.BasketVIew,basename="baskets")
router.register("baskets/item",views.BasketItemVIew,basename="basketitems")

urlpatterns = [
   
    path('register/',views.SignUpView.as_view()),
    path("token/",ObtainAuthToken.as_view())
    
] + router.urls