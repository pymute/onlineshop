from django.db import models
from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True, null=True)
    address = models.EmailField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username

class ShoppingCart(models.Model):
    column_3 = models.CharField(max_length=255, blank=True, default='')
    date = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def total_cost(self):
        return sum(product.price for product in self.products.all())

    def __str__(self):
        return f"Cart of {self.customer.user.username}"
    
class Customer(models.Model):
    shopcart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username
