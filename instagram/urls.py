from django.urls import path, re_path
from . import views

app_name = 'instagram'  # app name 을 지정하게 되면 url reverse 의 namespace 역할을 하게 된다.

urlpatterns = [
    path("", views.index, name='index'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    re_path(r'^(?P<username>[\w.@+-]+)/$', views.user_page, name='user_page')
]