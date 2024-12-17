from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()
    img=models.CharField(max_length=500)
    def __str__(self):
        return self.name
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE) 
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name