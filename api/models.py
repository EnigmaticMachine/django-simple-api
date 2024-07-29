from django.db import models


class AttributeName(models.Model):
    nazev = models.CharField(max_length=255)
    kod = models.CharField(max_length=255, blank=True, null=True)
    zobrazit = models.BooleanField(default=False)

    def __str__(self):
        return self.nazev


class AttributeValue(models.Model):
    hodnota = models.CharField(max_length=255)

    def __str__(self):
        return self.hodnota


class Attribute(models.Model):
    nazev_atributu = models.ForeignKey(AttributeName, on_delete=models.CASCADE)
    hodnota_atributu = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nazev_atributu} - {self.hodnota_atributu}"


class Product(models.Model):
    nazev = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    mena = models.CharField(max_length=10, blank=True, null=True)
    published_on = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.nazev


class ProductAttributes(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} - {self.attribute}"


class Image(models.Model):
    obrazek = models.URLField()
    nazev = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nazev if self.nazev else self.obrazek


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    obrazek = models.ForeignKey(Image, on_delete=models.CASCADE)
    nazev = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product} - {self.nazev}"


class Catalog(models.Model):
    nazev = models.CharField(max_length=255)
    obrazek = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name="catalog_image",
        blank=True,
        null=True,
    )
    products = models.ManyToManyField(Product)
    attributes = models.ManyToManyField(Attribute)

    def __str__(self):
        return self.nazev
