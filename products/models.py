from django.db import models
from users.models import User
# Create your models here.
class Cartegory(models.Model):
    cartegory_name = models.CharField(max_length=100, unique=True)
    cartegory_image = models.ImageField(upload_to="cartegories_group/", default="cartegories/kettle.png")
    def __str__(self):
        return self.cartegory_name
class Product(models.Model):
    title = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100)
    cartegory = models.ForeignKey(Cartegory, on_delete=models.CASCADE, to_field="cartegory_name")
    image = models.ImageField(upload_to="products_image")
    item_number = models.IntegerField()
    number_bought = models.IntegerField(default=0)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    product_details = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    offer = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    calculated_discount = models.IntegerField(default=0)
    exclusive = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    def save(self,*args, **kwargs):
        self.offer = True if self.discount > 0 else False
        self.trending = True if self.number_bought > 3 else False
        self.calculated_discount = self.discount / self.price * 100 
        super().save(*args, **kwargs)
class Review(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="review")
    title = models.CharField(max_length=100,)
    review =  models.TextField(default= "best quality and looks legit")
    star = models.IntegerField(default=0)
    user = models.CharField(max_length=200)
    review_date = models.DateTimeField(auto_now_add=True)
#  class Cart(models.)
    def __str__(self):
        return self.title

class CartegoryGroup(models.Model):
    group_name = models.CharField(max_length=200)
    cartegory = models.ForeignKey(Cartegory, on_delete=models.CASCADE)
    cartegory_image = models.ImageField(upload_to="cartegories_group/", default="cartegories/kettle.png")
    def __str__(self):
        return self.group_name

    
class Order(models.Model):
    choices = {
        "Delivered": "Delivered",
        "Pending": "Pending",
        "Rejected": "Rejected"
    }
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    item = models.IntegerField()
    image_url = models.URLField()
    status =  models.CharField(choices=choices, default=choices["Pending"], max_length=150)
    username = models.CharField(max_length=150)
    productId = models.IntegerField(default=1)
    def __str__(self):
        return self.title
