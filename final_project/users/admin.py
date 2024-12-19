from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'favorite_model')
    search_fields = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'favorite_model')}),
        ("Дополнительные данные", {'fields': ('first_name', 'last_name')})
    )
