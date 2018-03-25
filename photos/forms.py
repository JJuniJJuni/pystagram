from __future__ import unicode_literals
from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        field = ("image", "content")
