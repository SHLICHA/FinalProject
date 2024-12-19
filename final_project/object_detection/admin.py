from django.contrib import admin

from .models import DetectedObject, Object


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('user__username', 'pub_date')
    search_fields = ('username',)
    readonly_fields = ('pub_date',)


@admin.register(DetectedObject)
class DetectedObjectAdmin(admin.ModelAdmin):
    list_display = ('model', 'original_image__user__username',)
    search_fields = ('username',)
    readonly_fields = ('original_image', 'object_type', 'confidence', 'location')
