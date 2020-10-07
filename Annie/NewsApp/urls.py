from django.urls import path
from .views import NewsP, Home, Contact, NewsDate, Register, AddUser

urlpatterns = [
    path("", Home, name="home"),
    path("news/", NewsP, name="news"),
    path('newsdate/<int:year>', NewsDate, name='newsdate'),
    path("contact/", Contact, name="contact"),
    path("signup/", Register, name='register'),
    path("AddUser/", AddUser, name='adduser'),


]
