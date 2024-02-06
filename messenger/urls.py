from django.urls import path
from messenger import views

urlpatterns=[
    path('',views.home,name="homeScreen"),
    path('<str:name>',views.home2,name="dynamic")
]