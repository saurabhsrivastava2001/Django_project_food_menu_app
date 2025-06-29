from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name
    user_name= models.ForeignKey(User,on_delete=models.CASCADE,default=1)  # There is a link between this model (e.g., Item) and another model (User).In database terms: Item table has a column like user_id pointing to User table's id.
    item_name =models.CharField(max_length=100)
    item_desc = models.CharField(max_length=200)
    item_price= models.IntegerField()
    item_image=models.CharField(max_length=500,default="https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png")
    


#Tells Django: “If someone asks for the URL of this object, where should I send them?” 
# redirect after saving: return redirect(item)works if model has get_absolute_url()--
# This is a special method Django looks for. If it exists, Django can use it to find the URL of an item)
    def get_absolute_url(self):
        return reverse("food:detail",kwargs={'pk':self.pk})
    
#kwargs={'pk': self.pk}
#You're saying: “Give me the URL for this item’s detail page using its pk (primary key)”.