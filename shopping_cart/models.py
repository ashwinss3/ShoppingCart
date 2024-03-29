from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    """
    Base model for all models. Consists of common fields applcable to all models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    # Using Django's default User model. Any extra fields required can be added below.
    pass


class Product(models.Model, BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True, null=True)
    available_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model, BaseModel):
    # More fields can be added like order status, timestamps, etc.

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


class OrderItem(models.Model, BaseModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"


class Payment(models.Model, BaseModel):
    order = models.OneToOneField(Order, on_delete=models.PROTECT)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    # Add more fields such as payment status, timestamps, etc.

    def __str__(self):
        return f"Payment for Order #{self.order.id} ({self.amount_paid} USD)"
