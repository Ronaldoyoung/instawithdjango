from django.urls import path
from . import views
app_name = 'instagram' # app name 을 지정하게 되면 url reverse 의 namespace 역할을 하게 된다.

urlpatterns = [
    path('post/new/', views.post_new, name='post_new')
]