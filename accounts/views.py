from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import SignupForm
# Create your views here.

login = LoginView.as_view(template_name="accounts/login_form.html")



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            messages.success(request, "회원가입 환영합니다.")
            signed_user.send_welcome_email() # FIXME: Celery 로 처리 하는 것을 추천
            next_url = request.GET.get("next", '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })