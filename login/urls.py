from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="face-home"),
    path('login/',views.login,name="face-login"),
    path('postsign/',views.postsign,name="face-welcome")
]