from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name='login'), # /accounts/login/ => settings.LOGIN_URL
    path('signup/', views.signup, name='signup'),
]