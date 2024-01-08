from django.shortcuts import render

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from vendor.serializer import LoginSerializers

# Create your views here.


class LoginView(APIView):
    #POST METHOD REG ONLY 
    def post(self,request,*args,**kwargs):
        serializer=LoginSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
           
            return Response(data=serializer.data)
        else:
             return Response(data=serializer.errors)
        

        