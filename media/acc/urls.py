from django.urls import path
from . import views
urlpatterns = [
    path('', views.SignUp_views, name="SignUp")
]
