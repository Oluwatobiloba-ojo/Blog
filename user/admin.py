from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


# Register your models here.

@admin.register(models.BlogUser)
class UserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email"),
            },
        ),
    )

