from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.shortcuts import render


# Create your views here.
def profile(request, username):
    # url에서 username을 변수로 전해줬으므로, 매개변수로 받아야함
    User = get_user_model()
    # settings.py 모듈의 AUTH_USER_MODEL 설정 항목 기준으로
    # django 프로젝트가 사용하는 이용자 모델을 가져온다.
    user = get_object_or_404(User, username=username)
    # django에서 제공하는 User 모델을 사용하므로
    # 이 모델의 username 모델 필드를 검색하는데 사용하여 이용자 찾는다
    # 첫번 째 인자(지정한 모델)과 두번째 인자(검색 조건)으로 데이터 가져

    # 연결 당하는 쪽은 해당 필드를 갖고 있지 않음
    # 그래서 연결 당하는 쪽인 User 모델에 대한 접근 경로를
    # QuerySet 객체 속성으로 만들어 줌.
    # QuerySet은 사용자의 요청을 받아 질의를 생성.
    # 이 객채로 요청을 주고 받을 수 있음!!
    photos = user.photo_set.order_by('-created_at', '-pk')
    ctx = {
        'photos': photos,
        'user': user,
    }

    return render(request, 'profile.html', ctx)
