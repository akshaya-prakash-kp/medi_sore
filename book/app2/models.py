from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=210)
    author = models.CharField(max_length=111)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=4)
    image = models.CharField(max_length=2083, blank=True, default=0)
    book_available = models.BooleanField(default=False)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Books)
    total_price = models.DecimalField(max_digits=10, decimal_places=5)


class CartItems(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.book.price * self.quantity
