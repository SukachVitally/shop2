from django.db import models

class ProductGroup(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    group = models.ForeignKey(ProductGroup)

    def __str__(self):
        return self.name

