from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myapp(request):
    return HttpResponse('Hi Ashok!!')
