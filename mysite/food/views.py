from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello world I am saurabh!')

def item(request):
    return HttpResponse('this is my item!')
