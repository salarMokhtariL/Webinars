from django.shortcuts import render


# Create your views here.


def SignUp_views(request):
    contex = {}
    return render(request, 'signUp.html', contex)