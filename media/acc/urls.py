from django.urls import path
from . import views



urlpatterns = [
    path('', views.Index, name="Index"),
    path('Signin/', views.SignIn_views, name="Signin"),
    path('message/', views.Message_views, name="message"),

]
