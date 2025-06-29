from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=[
            'user_name','item_name','item_desc','item_price','item_image'
        ]