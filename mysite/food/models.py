from django.db import models

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name

    item_name =models.CharField(max_length=100)
    item_desc = models.CharField(max_length=200)
    item_price= models.IntegerField()
    item_image=models.CharField(max_length=500,default="https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png")
    
