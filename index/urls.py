from django.conf.urls import url
from . import views
from django.urls import path
from . import views
from .views import SignUpView, SignInView, SignOutView
from django.conf.urls import * 
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$',views.post_list, name='indesssx'),
    path('Login', views.Login, name='Login'),

    url(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
    url(r'^incia-sesion/$', SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),
    

]
