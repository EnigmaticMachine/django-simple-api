# import pytest
# from api.models import (
#     AttributeName,
#     AttributeValue,
#     Attribute,
#     Product,
#     ProductAttributes,
#     Image,
#     ProductImage,
#     Catalog,
# )


# @pytest.fixture
# def create_test_data():
#     # Create necessary Attribute Names
#     attr_name2 = AttributeName.objects.create(
#         id=2, nazev="Odolnost", kod="durability", zobrazit=False
#     )
#     attr_name4 = AttributeName.objects.create(
#         id=4, nazev="displej", kod=None, zobrazit=True
#     )
#     attr_name6 = AttributeName.objects.create(
#         id=6, nazev="Sleva", kod=None, zobrazit=False
#     )
#     attr_name7 = AttributeName.objects.create(
#         id=7, nazev="Určení", kod=None, zobrazit=True
#     )

#     # Create necessary Attribute Values
#     attr_value1 = AttributeValue.objects.create(id=1, hodnota="modrá")
#     attr_value4 = AttributeValue.objects.create(id=4, hodnota="růžová")
#     attr_value11 = AttributeValue.objects.create(id=11, hodnota="malá")
#     attr_value13 = AttributeValue.objects.create(id=13, hodnota="velká")
#     attr_value18 = AttributeValue.objects.create(id=18, hodnota="jemný")
#     attr_value19 = AttributeValue.objects.create(id=19, hodnota="ano")
#     attr_value20 = AttributeValue.objects.create(id=20, hodnota="ne")
#     attr_value21 = AttributeValue.objects.create(id=21, hodnota="pánské")
#     attr_value22 = AttributeValue.objects.create(id=22, hodnota="dámské")
#     attr_value23 = AttributeValue.objects.create(id=23, hodnota="dětské")

#     # Create necessary Attributes
#     attr2 = Attribute.objects.create(
#         id=2, nazev_atributu=attr_name2, hodnota_atributu=attr_value1
#     )
#     attr4 = Attribute.objects.create(
#         id=4, nazev_atributu=attr_name2, hodnota_atributu=attr_value4
#     )
#     attr6 = Attribute.objects.create(
#         id=6, nazev_atributu=attr_name4, hodnota_atributu=attr_value19
#     )
#     attr7 = Attribute.objects.create(
#         id=7, nazev_atributu=attr_name7, hodnota_atributu=attr_value21
#     )
#     attr11 = Attribute.objects.create(
#         id=11, nazev_atributu=attr_name2, hodnota_atributu=attr_value11
#     )
#     attr13 = Attribute.objects.create(
#         id=13, nazev_atributu=attr_name2, hodnota_atributu=attr_value13
#     )
#     attr18 = Attribute.objects.create(
#         id=18, nazev_atributu=attr_name4, hodnota_atributu=attr_value18
#     )
#     attr19 = Attribute.objects.create(
#         id=19, nazev_atributu=attr_name4, hodnota_atributu=attr_value19
#     )
#     attr21 = Attribute.objects.create(
#         id=21, nazev_atributu=attr_name7, hodnota_atributu=attr_value21
#     )
#     attr22 = Attribute.objects.create(
#         id=22, nazev_atributu=attr_name7, hodnota_atributu=attr_value22
#     )
#     attr23 = Attribute.objects.create(
#         id=23, nazev_atributu=attr_name6, hodnota_atributu=attr_value19
#     )
#     attr24 = Attribute.objects.create(
#         id=24, nazev_atributu=attr_name6, hodnota_atributu=attr_value20
#     )
#     attr26 = Attribute.objects.create(
#         id=26, nazev_atributu=attr_name7, hodnota_atributu=attr_value22
#     )
#     attr27 = Attribute.objects.create(
#         id=27, nazev_atributu=attr_name7, hodnota_atributu=attr_value23
#     )

#     # Create necessary Products
#     product1 = Product.objects.create(
#         id=1,
#         nazev="Whirlpool B TNF 5323 OX",
#         description="Volně stojící kombinovaná lednička se šestým smyslem. Díky tomuto šestému smyslu FreshLock dokáže obnovit teplotu 5× rychleji",
#         cena="21566",
#         mena="CZK",
#         is_published=False,
#     )
#     product2 = Product.objects.create(
#         id=2,
#         nazev="Vans Old Skool black",
#         description="Tohle prostě musíš mít. Unisex boty Vans Old Skool jsou snad povinnost pro každého skejťáka a rockera tělem i duší. Tradiční konstrukce a vzhled prostě nezklame",
#         cena="1466.00",
#         mena="CZK",
#         published_on="2018-01-15T00:00:00Z",
#         is_published=False,
#     )
#     product3 = Product.objects.create(
#         id=3,
#         nazev="Daniel Wellington DW00100164",
#         description="Módní hodinky Daniel Wellington z kolekce Classic Petite Sterling. Ideální doplněk pro ženy upřednostňující analogové a kulaté hodinky",
#         cena="11278.00",
#         mena="CZK",
#         published_on="2017-11-15T00:55:00Z",
#         is_published=True,
#     )
#     product4 = Product.objects.create(
#         id=4,
#         nazev="Tempish Dream Lady",
#         description="Elegantní, zateplené, pohodlné dámské lední brusle v tradičním bílém provedení. Ideální pro rekreační bruslení. Uvnitř se můžete těšit na anatomickou bandáž s pamětí",
#         cena="986.00",
#         mena="CZK",
#         is_published=False,
#     )
#     product5 = Product.objects.create(
#         id=5,
#         nazev="Funko Pop God of War Kratos",
#         description="Kratos, otec Atrea, se dočkal své vinylové POP! figurky od společnosti Funko.",
#         cena="800",
#         mena="CZK",
#         is_published=True,
#     )

#     # Create necessary ProductAttributes
#     ProductAttributes.objects.create(id=1, attribute=attr19, product=product1)
#     ProductAttributes.objects.create(id=2, attribute=attr4, product=product1)
#     ProductAttributes.objects.create(id=3, attribute=attr18, product=product1)
#     ProductAttributes.objects.create(id=4, attribute=attr6, product=product2)
#     ProductAttributes.objects.create(id=5, attribute=attr11, product=product2)
#     ProductAttributes.objects.create(id=6, attribute=attr21, product=product2)
#     ProductAttributes.objects.create(id=7, attribute=attr22, product=product1)
#     ProductAttributes.objects.create(id=8, attribute=attr7, product=product3)
#     ProductAttributes.objects.create(id=9, attribute=attr24, product=product3)
#     ProductAttributes.objects.create(id=10, attribute=attr21, product=product3)
#     ProductAttributes.objects.create(id=11, attribute=attr13, product=product3)
#     ProductAttributes.objects.create(id=12, attribute=attr26, product=product4)
#     ProductAttributes.objects.create(id=13, attribute=attr6, product=product4)
#     ProductAttributes.objects.create(id=14, attribute=attr21, product=product4)
#     ProductAttributes.objects.create(id=15, attribute=attr21, product=product5)
#     ProductAttributes.objects.create(id=16, attribute=attr2, product=product5)
#     ProductAttributes.objects.create(id=17, attribute=attr27, product=product5)

#     # Create necessary Images
#     image1 = Image.objects.create(
#         id=1, obrazek="https://free-images.com/or/4929/fridge_t_png.jpg"
#     )
#     image2 = Image.objects.create(
#         id=2,
#         nazev="plná lednice",
#         obrazek="https://free-images.com/or/ccc6/faulty_fridge_lighting_led_0.jpg",
#     )
#     image3 = Image.objects.create(
#         id=3, obrazek="https://free-images.com/md/df12/faulty_shelf_lighting_led.jpg"
#     )
#     image4 = Image.objects.create(
#         id=4, obrazek="https://free-images.com/lg/7687/blue_jay_bird_nature.jpg"
#     )
#     image5 = Image.objects.create(
#         id=5, obrazek="https://free-images.com/or/a09b/watch_time_ladies_watch_0.jpg"
#     )
#     image6 = Image.objects.create(
#         id=6, obrazek="https://free-images.com/md/faa5/teddy_bear_sheep_toys.jpg"
#     )

#     # Create necessary ProductImages
#     ProductImage.objects.create(
#         id=1, product=product1, obrazek=image1, nazev="hlavní foto"
#     )
#     ProductImage.objects.create(id=2, product=product1, obrazek=image2, nazev="galerie")
#     ProductImage.objects.create(
#         id=3, product=product2, obrazek=image3, nazev="hlavní foto"
#     )
#     ProductImage.objects.create(
#         id=4, product=product3, obrazek=image5, nazev="hlavní foto"
#     )
#     ProductImage.objects.create(
#         id=5, product=product5, obrazek=image6, nazev="hlavní foto"
#     )

#     # Create Catalogs
#     catalog1 = Catalog.objects.create(id=1, nazev="Výprodej 2018", obrazek=image4)
#     catalog1.products.set([product1, product2, product3, product4, product5])
#     catalog1.attributes.set([attr2, attr4, attr21, attr23])
