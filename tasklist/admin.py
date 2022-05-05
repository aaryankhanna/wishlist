from django.contrib import admin
from tasklist.models import User
from tasklist.models import Tasks

# Register your models here.
admin.site.register(User)
admin.site.register(Tasks)