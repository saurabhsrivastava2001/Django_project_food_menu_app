from django.shortcuts import render
from .models import Item
from django.http import HttpResponse
# Create your views here.
def index(request):
    item_list= Item.objects.all()
    context={
        'item_list':item_list,
    }
    return render(request,'food/index.html',context)

def item(request):
    return HttpResponse('this is my item!')

def contact (request):
    return HttpResponse(' this is my contact page')

def detail(request,item_id):
    item= Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'food/detail.html',context)