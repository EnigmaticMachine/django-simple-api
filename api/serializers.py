from rest_framework import serializers
from .models import (
    AttributeName,
    AttributeValue,
    Attribute,
    Product,
    ProductAttributes,
    Image,
    ProductImage,
    Catalog,
)


class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeName
        fields = "__all__"


class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = "__all__"


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributes
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


# class CatalogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Catalog
#         fields = "__all__"


class CatalogSerializer(serializers.ModelSerializer):
    products_ids = serializers.ListField(
        write_only=True, child=serializers.IntegerField(), source="products"
    )
    attributes_ids = serializers.ListField(
        write_only=True, child=serializers.IntegerField(), source="attributes"
    )

    class Meta:
        model = Catalog
        fields = ["nazev", "obrazek", "products_ids", "attributes_ids"]

    def create(self, validated_data):
        products_ids = validated_data.pop("products", [])
        attributes_ids = validated_data.pop("attributes", [])
        catalog = Catalog.objects.create(**validated_data)
        catalog.products.set(Product.objects.filter(id__in=products_ids))
        catalog.attributes.set(Attribute.objects.filter(id__in=attributes_ids))
        return catalog
