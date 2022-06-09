from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def get_photo_url(self):
        if self.cover and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/images/default.jpg"