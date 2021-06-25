from django import forms
from django.forms import fields
from .models import Uimage

class Imageform(forms.ModelForm):
    class Meta:
        model=Uimage
        fields= "__all__"
        labels= {"image":""}