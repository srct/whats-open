from django.http import Http404
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
def index(request):
    return render_to_response('management/index.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active and user.is_staff:
            login(request,user)
            return render_to_response('management/index.html')
        else:
             return render_to_response('403.html')
    else:
        return render_to_response('management/login.html') 
