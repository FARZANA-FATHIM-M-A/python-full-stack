from django.http import HttpResponse
from django.shortcuts import render
def a(request):
    a='<h1><center>Welcome Farzana</center></h1>'
    return HttpResponse(a)
# Create your views here.
