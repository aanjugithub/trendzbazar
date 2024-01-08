from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

