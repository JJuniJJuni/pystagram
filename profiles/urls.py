from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^(?P<username>[\w.@+-]+)/$',
        # '.'은 [] 안에 쓰면 그냥 점 자체를 말하는거임
        # [] 밖에서 써야만 임의의 한 문자
        # 다른애들도 마찬가지. []안에서 쓰면 본래의 의미로 쓰
        views.profile,
        name='profile'
    ),
]