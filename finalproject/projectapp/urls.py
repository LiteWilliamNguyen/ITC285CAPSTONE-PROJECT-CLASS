from django.urls import path
from . import views

#this is a comment
urlpatterns= [
    path('',views.index, name='index'),
    path('getProduct/', views.getProduct, name="product"),
    path('getMonk/', views.getMonk, name="monk"),
    path('getMember/', views.getMember, name="member"),
    path('loginmessage/',views.loginMessage, name='loginmessage'),
    path('logoutmessasge/', views.logoutMessage, name="logoutmessage"),
    path('newproduct/', views.newProduct, name="newproduct")
]
