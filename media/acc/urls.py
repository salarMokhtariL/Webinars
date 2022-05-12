from django.urls import path
from . import views
urlpatterns = [
    path('Signin/', views.SignIn_views, name="Signin")
]
