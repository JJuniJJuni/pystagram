from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from photos.views import create
from photos.views import hello
from photos.views import detail
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^hello/$', hello),
    url(r'^photos/(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r"^photos/upload/$", create, name="create"),
    url(r"^hidden-photos/(?P<pk>[0-9]+)/$", detail, kwargs={"hidden": True}),
    url(r'^admin/', admin.site.urls),
    url(
        r'^accounts/login/',
        auth_views.login,
        name='login',
        kwargs={
            'template_name': 'login.html'
            # 키가 template_name 이고, login.html 화면을 출력하도록
        }
    ),
    url(
        r'^accounts/logout/',
        auth_views.logout,
        name='logout',
        kwargs={
            'next_page': settings.LOGIN_URL,
            # 키가 next_page 이고, 다시 로그인 화면을 출력하도록
            # 이렇게 설정하지 않으면, 로그아웃 화면이 나타남!!
        }
    ),
]

urlpatterns += static('/upload_files/', document_root=settings.MEDIA_ROOT)

