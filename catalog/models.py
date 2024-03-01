from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class Brand(models.Model):
    name = models.CharField(max_length=255)
    foundation_year = models.PositiveIntegerField()
    country = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=255)
    type = models.ManyToManyField(Category, related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}, {self.brand}"
