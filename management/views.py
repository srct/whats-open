from django.http import Http404
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('management/index.html')
def login(requets):
    return render_to_response('management/login.html') 
