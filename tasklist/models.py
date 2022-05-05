from datetime import date
import email
from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    
    
    # def isexist(self):
    #     print(self)
    #     if User.objects.filter(email=self.email):

    #         return True
    #     return False


    # @staticmethod
    # def getuser(email):
    #     return User.objects.get(email=email)



    # def register(self):
    #     self.save()

class Tasks(models.Model):
    # email=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    deadline=models.DateTimeField()

    # @staticmethod
    def gettask(self):
        return Tasks.objects.filter(email=self.email)