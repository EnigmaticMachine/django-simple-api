from django.contrib import admin
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


@admin.register(AttributeName)
class AttributeNameAdmin(admin.ModelAdmin):
    list_display = ("nazev", "kod", "zobrazit")


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ("hodnota",)


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ("nazev_atributu", "hodnota_atributu")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "nazev",
        "description",
        "cena",
        "mena",
        "published_on",
        "is_published",
    )


@admin.register(ProductAttributes)
class ProductAttributesAdmin(admin.ModelAdmin):
    list_display = ("product", "attribute")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("obrazek", "nazev")


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "obrazek", "nazev")


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ("nazev", "obrazek")
    filter_horizontal = ("products", "attributes")
