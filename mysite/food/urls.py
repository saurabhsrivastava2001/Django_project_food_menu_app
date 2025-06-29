from . import views
from django.urls import path

app_name='food'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),#class based view index(list view)

    path('item/',views.item,name='item'),
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),#class based view , detail view
    #add items
    path ('add/',views.CreateItem.as_view(),name='create_item'),
    #update items
    path('update/<int:id>',views.update_item,name='update_item'),
    #delete url 
    path ('delete/<int:id>',views.delete_item,name='delete_item')
]
