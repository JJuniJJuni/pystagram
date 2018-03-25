from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from django.shortcuts import get_object_or_404
from .forms import PhotoForm
# Create your views here.


def hello(request):
    return HttpResponse("안녕하세요!")


def detail(request,pk,hidden=False):  # 'hidden' 이라는 변수 기본 값이 False!!
    if hidden is True:
        # todo: 뭔가 은밀한 작업을 합시다
        pass
    photo = get_object_or_404(Photo,pk=pk)

    messages = (
        "<p>{pk}번 사진 보여줄게요</p>".format(pk=photo.pk),
        "<p>주소는 {url}</p>".format(url=photo.image.url),
        "<p><img src={url} /></p>".format(url=photo.image.url),
    )
    return HttpResponse("\n".join(messages))


def create(request):
    form = PhotoForm()
    ctx = {
        "form": form,
    }
    return render(request, "edit.html", ctx)


