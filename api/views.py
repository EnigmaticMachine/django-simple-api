# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
from django.shortcuts import get_object_or_404

model_mapping = {
    "AttributeName": (AttributeName, AttributeNameSerializer),
    "AttributeValue": (AttributeValue, AttributeValueSerializer),
    "Attribute": (Attribute, AttributeSerializer),
    "Product": (Product, ProductSerializer),
    "ProductAttributes": (ProductAttributes, ProductAttributesSerializer),
    "Image": (Image, ImageSerializer),
    "ProductImage": (ProductImage, ProductImageSerializer),
    "Catalog": (Catalog, CatalogSerializer),
}


class ImportDataView(APIView):
    def post(self, request):
        data = request.data
        if isinstance(data, list):
            for item in data:
                for model_name, model_data in item.items():
                    model_class, serializer_class = model_mapping.get(
                        model_name, (None, None)
                    )
                    if model_class and serializer_class:
                        serializer = serializer_class(data=model_data)
                        if serializer.is_valid():
                            serializer.save()
                        else:
                            return Response(
                                serializer.errors, status=status.HTTP_400_BAD_REQUEST
                            )
                    else:
                        return Response(
                            {"error": "Unknown model name"},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
        else:
            return Response(
                {"error": "Invalid data format"}, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {"message": "Data imported successfully"}, status=status.HTTP_201_CREATED
        )


class ModelDetailListView(APIView):
    def get(self, request, model_name):
        model_class, serializer_class = model_mapping.get(model_name, (None, None))
        if model_class and serializer_class:
            queryset = model_class.objects.all()
            serializer = serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(
                {"error": "Unknown model name"}, status=status.HTTP_400_BAD_REQUEST
            )


class ModelDetailView(APIView):
    def get(self, request, model_name, pk):
        model_class, serializer_class = model_mapping.get(model_name, (None, None))
        if model_class and serializer_class:
            instance = get_object_or_404(model_class, pk=pk)
            serializer = serializer_class(instance)
            return Response(serializer.data)
        else:
            return Response(
                {"error": "Unknown model name"}, status=status.HTTP_400_BAD_REQUEST
            )
