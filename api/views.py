from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import UserSerializer,ProductSerializer,BasketItemSerializer,BasketSerializer
from rest_framework import viewsets
from api.models import Product,BasketItem
from rest_framework import serializers
from rest_framework import permissions,authentication
from rest_framework.decorators import action

# Create your views here.
#user creation -- registration
class SignUpView(APIView):

    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        
        return Response(data=serializer.errors)
    
class ProductView(viewsets.ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=ProductSerializer
    queryset=Product.objects.all() #list all objects       

    #customer side product creayte,update destroy acces denied only view n retrieve is accesabile for customer
    
    def create(self,request,*args,**kwargs):
        raise serializers.ValidationError("permission denied")
    
    def update(self,request,*args,**kwargs):
        raise serializers.ValidationError("permission denied")
    
    def destroy(self,request,*args,**kwargs):
        raise serializers.ValidationError("permission denied")
    
    #url:http://127.0.0.1:8000/api/products/{id}/add_to_basket/   
    # method:post   data:{qty}   authorization:Token

    @action(methods=["post"],detail=True)
    def add_to_basket(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        product_object=Product.objects.get(id=id)
        basket_object=request.user.cart
        serializer=BasketItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product_object,basket=basket_object)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
        
    
# 
#method:get
# data:nill
# authorization:Token
        
class BasketVIew(viewsets.ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=request.user.cart
        serializer=BasketSerializer(qs,many=False)
        return Response(data=serializer.data)
    

# http://127.0.0.1:8000/api/baskets/item/{id}/  _to update an item in basket
#method -get
#data nill
# authorization:Token
class BasketItemVIew(viewsets.ModelViewSet):                 #if inherited from model class only we needs to provide serializer class and queryset
        serializer_class=BasketItemSerializer
        queryset=BasketItem.objects.all()
        authentication_classes=[authentication.TokenAuthentication]
        permission_classes=[permissions.IsAuthenticated]

        def create(self,request,*args,**Kwargs):
            raise serializers.ValidationError("permission denied.............")






