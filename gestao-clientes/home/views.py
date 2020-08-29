from django.shortcuts import render, redirect
from django.contrib.auth import logout


def home(request):
    import pdb; 
    pdb.set_trace()
    a=10
    b=20
    c=a*10
    return render(request, 'home.html', {'result':c})


def my_logout(request):
    logout(request)
    return redirect('home')
