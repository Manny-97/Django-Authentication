from django.contrib import admin

from . import models

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "phone_number"
    )

admin.site.register(models.User, UserAdmin)
