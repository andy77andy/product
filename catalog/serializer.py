from rest_framework import serializers

from catalog.models import Category, Product, Brand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ProductForBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name",)


class BrandSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    products = ProductForBrandSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = ("id", "name", "country", "foundation_year", "category", "products")


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("id", "name", "brand", "price")


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("name", "products")