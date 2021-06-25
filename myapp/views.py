from django import forms
from django.shortcuts import render
from .forms import Imageform
from .models import Uimage

# Create your views here.
def home(request):
    if request.method != "GET":
        form=Imageform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = Imageform()
    img = Uimage.objects.all()
    return render(request,'myapp/home.html',{'img':img,'form':form})