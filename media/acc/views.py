from django.shortcuts import render


# Create your views here.



def Index(request):
    contex ={}
    return render(request, 'index.html', contex)
    

def SignIn_views(request):
    contex = {}
    return render(request, 'signUp.html', contex)


def Message_views(request):
    contex = {}
    return render(request, 'message.html', contex)