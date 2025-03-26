from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Task,User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('name','email','mobile')
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=('name','description','status','task_type')
