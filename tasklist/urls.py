# from django.urls import urls
from django.urls import URLPattern, path
from .views import *

urlpatterns=[
    path('',Signup.as_view(),name='signup'),
    path('index',Task.as_view(),name='index'),
    path('login',Login.as_view(),name='login')

]