from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from django.shortcuts import get_object_or_404
# Create your views here.

def hello(request):
    return HttpResponse("안녕하세요!")

def detail(request,pk):
    photo=get_object_or_404(Photo,pk=pk)

    messages=(
        "<p>{pk}번 사진 보여줄게요</p>".format(pk=photo.pk),
        "<p>주소는 {url}</p>".format(url=photo.image.url),
        "<p><img src={url} /></p>".format(url=photo.image.url),
    )
    return HttpResponse("\n".join(messages))