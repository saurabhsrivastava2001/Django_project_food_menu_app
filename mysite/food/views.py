from django.shortcuts import render ,redirect
from .models import Item
from django.http import HttpResponse
from .forms import ItemForm

#class based views 
from django.views.generic.list import ListView  #because the index view is listing the objects 

# Create your views here.
def index(request):
    item_list= Item.objects.all()
    context={
        'item_list':item_list,
    }
    return render(request,'food/index.html',context)

#class based views
class IndexView(ListView) :
    model=Item
    template_name='food/index.html'
    context_object_name='item_list'


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

def create_item(request):
    form = ItemForm(request.POST or None)

    # Debug print
    print("Request method:", request.method)

    if request.method == "POST":
        print("POST Data:", request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('food:index')
        else:
            print("Form errors:", form.errors)
    
    context = {'form': form }
    return render(request, 'food/item_form.html', context)

#updating the item 

def update_item(request,id):
    item= Item.objects.get(id=id)
    form= ItemForm(request.POST or None ,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render (request,'food/item_form.html',{'form':form,'item':item})

#deleting the item

def delete_item(request,id):
    item= Item.objects.get(id=id)

    if request.method=='POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/item_delete.html',{'item':item})