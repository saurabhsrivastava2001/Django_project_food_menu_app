from django.shortcuts import render ,redirect
from .models import Item
from django.http import HttpResponse
from .forms import ItemForm

#class based views 
from django.views.generic.list import ListView #because the index view is listing the objects 
from django.views.generic.detail import DetailView #for the fetail page
from django.views.generic.edit import CreateView
# Create your views here.
def index(request):
    item_list= Item.objects.all()
    context={
        'item_list':item_list,
    }
    return render(request,'food/index.html',context)

#class based views--list view
class IndexView(ListView) :
    model=Item # internallt django says - hey i want to show the lis tof the Item object
    #internally -- queryset= Item.objects.all()
    #automatically - context={'object_list':queryset}
    template_name='food/index.html'
    context_object_name='item_list' #here we oberwrite the name from object list to item_list 

{}
def item(request):
    return HttpResponse('this is my item!')

 
def detail(request,item_id):
    item= Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'f ood/detail.html',context)
#class based detailview

class FoodDetail(DetailView):
    model=Item
    template_name='food/detail.html'


def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == "POST":
        print("POST Data:", request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('food:index')
        else:
            print("Form errors:", form.errors)
    context = {'form': form }
    return render(request, 'food/item_form.html', context)

#class based view of creating the items

class CreateItem(CreateView):
    model=Item
    fields=['item_name','item_desc','item_price','item_image']
    template_name='food/item_form.html'

    #saving 
    def form_valid(self, form):
        form.instance.user_name=self.request.user
        return super().form_valid(form)
    '''
        What does super().form_valid(form) do?
        self.object = form.save()  # ← YES! this is where it saves to the DB  (super() bcz its calling the parent method -- CreateView 
        return HttpResponseRedirect(self.get_success_url())
    '''
    
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