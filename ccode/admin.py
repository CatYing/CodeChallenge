from django.contrib import admin
from models import *
# Register your models here.


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('realname', 'pass_num', 'start_time', 'end_time')
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Solution)