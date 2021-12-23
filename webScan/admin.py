from django.contrib import admin

from .models import User

# 注册后台表User管理
admin.site.register(User)