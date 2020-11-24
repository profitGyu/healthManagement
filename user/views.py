from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import CreateView

from user.forms import UserRegistrationForm
from user.models import User


def hello(request, to):                    # 핸들러 선언. 언제나 첫번쨰 인자는 request 객체입니다..
    return HttpResponse('Hello world {}'.format(to)) # 핸들러의 반환값. httpResponse 함수를 통해 문자열을 반환합니다.

# 인덱스로 가는 뷰
class Index(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'common/index.html'
        return render(request, template_name)
# 회원 가입 뷰 생성

class UserRegistrationView(CreateView):
    model = get_user_model()
    form_class = UserRegistrationForm
    success_url = '/user/login/'
    verify_url = '/user/verify/'
    token_generator = default_token_generator
    template_name = "user/login_form.html"


class UserLoginView(LoginView):

    template_name = "user/user_form.html"
    def form_valid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_valid(form)


