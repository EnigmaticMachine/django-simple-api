from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AttributeNameViewSet,
    AttributeValueViewSet,
    AttributeViewSet,
    ProductViewSet,
    ProductAttributesViewSet,
    ImageViewSet,
    ProductImageViewSet,
    CatalogViewSet,
)

router = DefaultRouter()
router.register(r"attributenames", AttributeNameViewSet)
router.register(r"attributevalues", AttributeValueViewSet)
router.register(r"attributes", AttributeViewSet)
router.register(r"products", ProductViewSet)
router.register(r"productattributes", ProductAttributesViewSet)
router.register(r"images", ImageViewSet)
router.register(r"productimages", ProductImageViewSet)
router.register(r"catalogs", CatalogViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
