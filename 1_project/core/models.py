from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model



class Category(models.Model):
    category_creator     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category_en          = models.CharField(max_length=34, default='-')
    category_bn          = models.CharField(max_length=34, default='-')
    category_description = models.TextField(null=True, blank=True)
    photo                = models.ImageField(upload_to='img/category/', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_en


class Item(models.Model):
    photo                = models.ImageField(upload_to='img/products/', null=True, blank=True)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username