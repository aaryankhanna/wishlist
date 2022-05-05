from ast import Index
import email
from operator import index
from unicodedata import name
from django.shortcuts import redirect, render,HttpResponseRedirect
from .models import User
from .models import Tasks
from django.views import View
from django.http import HttpResponse


# Create your views here.
class Signup(View):
    def get(self,request):
        return render(request,'signup.html')

    def post(self,request):
        # userdata=request.POST
        # name=userdata.get('name')
        name=request.POST['name']
        
        # email=userdata.get('email')
        email=request.POST['email']
        # password=userdata.get('password')
        password=request.POST['password']
        print(name,email,password)
        if User.objects.filter(email=email):
            return HttpResponse('email exists')
        user= User(name=name,email=email,password=password) 
        print(user)
        user.save()
        # if not user.isexist():
        #     user.save()

        # values={
        #     'name':name,
        #     'email':email,
        #     'password':password
        # }
        
        return redirect('index')

class Login(View):

    def get(self, request):
        return render(request,'login.html')

    def post(self, request):
        err=None
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.getuser(email)
        print(user)
        if user:
            if user.password==password:
                return HttpResponseRedirect('index')
            else:
                err='Invalid password'
        else:
            err='Invalid email'


        values={
            # 'err':err,
            'email':email,
            'password':password
        }
        return render(request,'login.html',{'err':err})




class Task(View):
    def get(self, request):
        # email=request.POST.get('email')
        # # email=request.get('email')
        # print(email)
        task=Tasks.objects.all()
        task=dict(task)
        return render(request,'index.html',task)