from django.urls import path
from .views import *
urlpatterns=[
    path('login/',login_manage),
    path('timing/',timing),
    path('show_user/',show_user),
    path('search_user/',search_user)
]