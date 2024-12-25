from django import forms

from .models import Object


class ObjectForm(forms.ModelForm):
    """Форма добавления изображения"""
    class Meta:
        model = Object
        fields = ('model', 'source_image')
