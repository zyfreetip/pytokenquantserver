from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .modesl import BlockUser
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LoginForm
from django.views.generic.base import View

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user=BlockUser.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
            except Exception as e:
                return None

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        pre_check = login_form.is_valid()
        if pre_check:
            user_name = request.POST.get('username', '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'signup.html', {'signup_form': signup_form,'msg':'用户已经存在'})
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'msg': u'用户名或者密码错误'})
        else:
            return render(request, 'login.html', {'login.html':login_form})
