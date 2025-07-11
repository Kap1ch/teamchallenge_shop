from django.db import models

from apps.core.models import BaseModel

# Create your models here.

class Orders(BaseModel):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    orders_date = models.DateTimeField(auto_now_add=True, verbose_name="Orders date")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total price")
    quantity =  models.IntegerField(verbose_name="Quantity")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending", verbose_name="Order status")

    def __str__(self):
        return f"Order #{self.id} - {self.get_status_display()}"