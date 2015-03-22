from django.db import models


class ProductGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)

    def info(self):
        return self.productinfo_set.all()

    def groups(self):
        relations = self.productgrouprelation_set.all()
        return list(map(lambda relation: relation.group, relations))

    def __str__(self):
        return self.name


class ProductGroupRelation(models.Model):
    group = models.ForeignKey(ProductGroup)
    product = models.ForeignKey(Product)


class ProductInfoType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductInfo(models.Model):
    content = models.TextField()
    product = models.ForeignKey(Product)
    type = models.ForeignKey(ProductInfoType)

    def __str__(self):
        return self.content
