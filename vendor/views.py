from django.shortcuts import render,redirect
from vendor.forms import LoginForm,UserForm
from django.views.generic import View
from django.contrib.auth import login,logout,authenticate



# Create your views here.

#registration view
class RegistartionView(View):
    def get(self,request,*args,**kwargs):
        form=UserForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=UserForm(request.POST)
        if form.is_valid():

            form.save()
            print("registration success...")
            return redirect('register')
        else:
            print("error in registration....")
            return render(request,"register.html",{"form":form})
        


class LogInView(View):
    def get(self,request,*args,**Kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
     
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(uname,pwd,"-------------")
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                print("--------- valid credentials-----")
                login(request,user_object)
                return redirect("index")
            
        print("invalid login...........")
        return render(request,"login.html",{"form":form})
    