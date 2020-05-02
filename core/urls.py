from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('index', views.index, name='index'),
    path('login', views.LoginView.as_view(), name='login'),
]

