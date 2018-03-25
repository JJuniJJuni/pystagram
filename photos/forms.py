from __future__ import unicode_literals
from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ("filtered_image",)  # 이 파일 빼고
