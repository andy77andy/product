from django.shortcuts import render
from rest_framework import viewsets

from catalog.models import Category, Brand, Product
from catalog.serializer import CategorySerializer, BrandSerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet,):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandViewSet(viewsets.ModelViewSet,):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
