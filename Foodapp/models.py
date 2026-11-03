from django.db import models

# Create your models here.
class FoodDb(models.Model):
    food_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    restaurant_name = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)


class OrderDb(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    mobile = models.CharField(max_length=15)
    food_id = models.IntegerField()
    food_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=50)
    ordered_at = models.DateTimeField(auto_now_add=True)