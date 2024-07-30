# your_app/views.py

from rest_framework import viewsets
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
from .serializers import (
    AttributeNameSerializer,
    AttributeValueSerializer,
    AttributeSerializer,
    ProductSerializer,
    ProductAttributesSerializer,
    ImageSerializer,
    ProductImageSerializer,
    CatalogSerializer,
)


class AttributeNameViewSet(viewsets.ModelViewSet):
    queryset = AttributeName.objects.all()
    serializer_class = AttributeNameSerializer


class AttributeValueViewSet(viewsets.ModelViewSet):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAttributesViewSet(viewsets.ModelViewSet):
    queryset = ProductAttributes.objects.all()
    serializer_class = ProductAttributesSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
