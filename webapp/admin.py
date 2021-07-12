from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from webapp.models import CustomUser

# para encriptar a pass
class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)