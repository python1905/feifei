from django.conf.urls import url

from login import views

urlpattenrs = [
    url(r'^login/$', views.login, name='login')
]