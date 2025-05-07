from django.contrib import admin

from .models import Card, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'created_at')


class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Card, CardAdmin)
