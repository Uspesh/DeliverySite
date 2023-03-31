from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Menu(models.Model):
    title = models.CharField(max_length=100)

    url_name = models.CharField(max_length=50, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')


    def __str__(self):
        return self.title


    class Meta:
        ordering = ['id']

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, unique=True)
    about = models.TextField()
    price = models.IntegerField(default=1000)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('element', kwargs={'element_slug': self.slug})

    def get_absolute_url_cart(self):
        return reverse('cart:cart_add', args=[self.pk])

    class Meta:
        ordering = ['id']

class Category(models.Model):
    category = models.CharField(max_length=40)
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.category

class GetUserInfo(User):
    name = models.CharField(max_length=40)
    tel_num = models.IntegerField()
    address = models.TextField()

    USERNAME_FIELD = 'name'