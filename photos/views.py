from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from django.shortcuts import get_object_or_404
from .forms import PhotoForm
from django.shortcuts import redirect
# Create your views here.


def hello(request):
    return HttpResponse("안녕하세요!")


def detail(request, pk, hidden=False):  # 'hidden' 이라는 변수 기본 값이 False!!
    if hidden is True:
        # todo: 뭔가 은밀한 작업을 합시다
        pass
    photo = get_object_or_404(Photo, pk=pk)
    # photo 객체를 가져오고,없으면, 404 페이지 뜨게끔
    messages = (
        "<p>{pk}번 사진 보여줄게요</p>".format(pk=photo.pk),
        "<p>주소는 {url}</p>".format(url=photo.image.url),
        "<p><img src={url} /></p>".format(url=photo.image.url),
    )
    return HttpResponse("\n".join(messages))


def create(request):
    if request.method == "GET":
        # '/photo/upload'에 HTTP GET 방식으로 접근
        # 사진 게시물을 작성하는 화면이 나옴
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return redirect(obj)
    ctx = {
        "form": form,
    }
    return render(request, "edit.html", ctx)


