import email
from unicodedata import name
from django.shortcuts import render,HttpResponseRedirect
from .models import User
from .models import Tasks
from django.views import View


# Create your views here.
class Signup(View):
    def get(self,request):
        return render(request,'signup.html')

    def post(self,request):
        userdata=request.POST
        name=userdata.get('name')
        email=userdata.get('email')
        password=userdata.get('password')
        user= User(name=name,email=email,password=password) 
        if not user.isexist():
            user.register()

        values={
            'name':name,
            'email':email,
            'password':password
        }

        return render(request,'signup.html',values)

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