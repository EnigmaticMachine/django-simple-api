import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from api.models import (
    AttributeName,
    AttributeValue,
    Attribute,
    Product,
    Image,
    ProductImage,
    Catalog,
)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def attribute_name():
    return AttributeName.objects.create(nazev="Barva")


@pytest.fixture
def attribute_value():
    return AttributeValue.objects.create(hodnota="modrá")


@pytest.fixture
def attribute(attribute_name, attribute_value):
    return Attribute.objects.create(
        nazev_atributu=attribute_name, hodnota_atributu=attribute_value
    )


@pytest.fixture
def product():
    return Product.objects.create(
        nazev="Whirlpool B TNF 5323 OX",
        description="Volně stojící kombinovaná lednička se šestým smyslem.",
        cena="21566",
        mena="CZK",
    )


@pytest.fixture
def image():
    return Image.objects.create(
        obrazek="https://free-images.com/or/4929/fridge_t_png.jpg"
    )


@pytest.fixture
def product_image(product, image):
    return ProductImage.objects.create(
        product=product, obrazek=image, nazev="hlavní foto"
    )


@pytest.fixture
def catalog(image, product, attribute):
    catalog = Catalog.objects.create(nazev="Výprodej 2018", obrazek=image)
    catalog.products.add(product)
    catalog.attributes.add(attribute)
    return catalog


@pytest.mark.django_db
def test_import_data(api_client):
    url = reverse("import_data")
    data = [
        {"attribute_name": {"nazev": "Barva"}},
        {"attribute_value": {"hodnota": "modrá"}},
        {"attribute_value": {"hodnota": "zelená"}},
        {"attribute_value": {"hodnota": "žlutá"}},
        {"attribute": {"nazev_atributu": 1, "hodnota_atributu": 1}},
        {"attribute": {"nazev_atributu": 1, "hodnota_atributu": 2}},
        {"attribute": {"nazev_atributu": 1, "hodnota_atributu": 3}},
        {
            "product": {
                "nazev": "Whirlpool B TNF 5323 OX",
                "description": "Volně stojící kombinovaná lednička se šestým smyslem.",
                "cena": "21566",
                "mena": "CZK",
                "published_on": None,
                "is_published": False,
            }
        },
        {"image": {"obrazek": "https://free-images.com/or/4929/fridge_t_png.jpg"}},
        {
            "image": {
                "nazev": "plná lednice",
                "obrazek": "https://free-images.com/or/ccc6/faulty_fridge_lighting_led_0.jpg",
            }
        },
        {"product_image": {"product": 1, "obrazek": 1, "nazev": "hlavní foto"}},
        {
            "catalog": {
                "nazev": "Výprodej 2018",
                "obrazek": 2,
                "products_ids": [1],
                "attributes_ids": [1, 2, 3],
            }
        },
    ]

    logger.debug(f"Request data: {data}")

    response = api_client.post(url, data, format="json")

    logger.debug(f"Response status code: {response.status_code}")
    logger.debug(f"Response content: {response.content}")

    assert response.status_code == status.HTTP_201_CREATED

    catalog = Catalog.objects.get(nazev="Výprodej 2018")
    assert catalog.nazev == "Výprodej 2018"
    assert catalog.obrazek.id == 2
    assert catalog.obrazek.nazev == "plná lednice"
    assert list(catalog.products.values_list("id", flat=True)) == [1]
    mena = catalog.products.all()[0].mena
    assert mena == "CZK"
    assert list(catalog.attributes.values_list("id", flat=True)) == [1, 2, 3]
    second_attribute = catalog.attributes.all()[1]
    value = second_attribute.hodnota_atributu.hodnota
    assert value == "zelená"

    attr3 = Attribute.objects.get(id=3)
    assert attr3.nazev_atributu_id == 1
    assert attr3.hodnota_atributu_id == 3
    assert attr3.hodnota_atributu.hodnota == "žlutá"


@pytest.mark.django_db
def test_model_detail_list(api_client):
    # Initial data
    AttributeName.objects.create(nazev="Initial Attribute")

    # Test initial length
    url = reverse("model_detail_list", args=["attribute_name"])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

    # Add more data and test length
    AttributeName.objects.create(nazev="Second Attribute")
    AttributeName.objects.create(nazev="Third Attribute")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3

    # Test different model
    AttributeValue.objects.create(hodnota="Initial Value")
    url = reverse("model_detail_list", args=["attribute_value"])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

    # Add more data to different model and test length
    AttributeValue.objects.create(hodnota="Second Value")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2


@pytest.mark.django_db
def test_import_invalid_data_format(api_client):
    url = reverse("import_data")

    # Invalid data: missing 'nazev' in AttributeName
    invalid_data_1 = [
        {"attribute_name": {"kod": "color"}},
        {"attribute_value": {"hodnota": "modrá"}},
    ]
    response = api_client.post(url, invalid_data_1, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data: missing 'nazev_atributu' in Attribute
    invalid_data_2 = [
        {"attribute_name": {"nazev": "Barva"}},
        {"attribute_value": {"hodnota": "modrá"}},
        {"attribute": {"hodnota_atributu": 1}},
    ]
    response = api_client.post(url, invalid_data_2, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data: missing 'nazev' in Product
    invalid_data_3 = [
        {
            "product": {
                "description": "Some product description",
                "cena": "123.45",
                "mena": "CZK",
            }
        }
    ]
    response = api_client.post(url, invalid_data_3, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data: missing 'product' in ProductAttributes
    invalid_data_4 = [{"product_attributes": {"attribute": 1}}]
    response = api_client.post(url, invalid_data_4, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data: missing 'obrazek' in Image
    invalid_data_5 = [{"image": {"nazev": "Image Name"}}]
    response = api_client.post(url, invalid_data_5, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data: missing 'product' in ProductImage
    invalid_data_6 = [{"product_image": {"obrazek": 1, "nazev": "Main Photo"}}]
    response = api_client.post(url, invalid_data_6, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data: missing 'products_ids' in Catalog
    invalid_data_7 = [
        {
            "catalog": {
                "nazev": "Výprodej 2018",
                "obrazek": 1,
                "attributes_ids": [1, 2, 3],
            }
        }
    ]
    response = api_client.post(url, invalid_data_7, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data: missing 'attributes_ids' in Catalog
    invalid_data_8 = [
        {"catalog": {"nazev": "Výprodej 2018", "obrazek": 1, "products_ids": [1, 2, 3]}}
    ]
    response = api_client.post(url, invalid_data_8, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_import_invalid_names_in_data(api_client):
    url = reverse("import_data")

    # Invalid data: wrong key in AttributeName
    invalid_data_1 = [
        {"attribute_name": {"name": "Barva"}},  # 'name' should be 'nazev'
        {"attribute_value": {"hodnota": "modrá"}},
    ]
    response = api_client.post(url, invalid_data_1, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data: wrong key in AttributeValue
    invalid_data_2 = [
        {"attribute_name": {"nazev": "Barva"}},
        {"attribute_value": {"value": "modrá"}},  # 'value' should be 'hodnota'
    ]
    response = api_client.post(url, invalid_data_2, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data: wrong key in Attribute
    invalid_data_3 = [
        {"attribute_name": {"nazev": "Barva"}},
        {"attribute_value": {"hodnota": "modrá"}},
        {
            "attribute": {"atribut_nazev": 1, "hodnota_atributu": 1}
        },  # 'atribut_nazev' should be 'nazev_atributu'
    ]
    response = api_client.post(url, invalid_data_3, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data: wrong key in Product
    invalid_data_4 = [
        {
            "product": {
                "name": "Product 1",  # 'name' should be 'nazev'
                "description": "Some product description",
                "cena": "123.45",
                "mena": "CZK",
            }
        }
    ]
    response = api_client.post(url, invalid_data_4, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data: wrong key in ProductAttributes
    invalid_data_5 = [
        {"product_attributes": {"product_id": 1, "attribute": 1}}
    ]  # 'product_id' should be 'product'
    response = api_client.post(url, invalid_data_5, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data: wrong key in Image
    invalid_data_6 = [
        {"image": {"image": "http://example.com/image.jpg", "nazev": "Image Name"}}
    ]  # 'image' should be 'obrazek'
    response = api_client.post(url, invalid_data_6, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data: wrong key in ProductImage
    invalid_data_7 = [
        {"product_image": {"product_id": 1, "obrazek": 1, "nazev": "Main Photo"}}
    ]  # 'product_id' should be 'product'
    response = api_client.post(url, invalid_data_7, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data: wrong key in Catalog
    invalid_data_8 = [
        {
            "catalog": {
                "title": "Výprodej 2018",  # 'title' should be 'nazev'
                "obrazek": 1,
                "products_ids": [1, 2, 3],
                "attributes_ids": [1, 2, 3],
            }
        }
    ]
    response = api_client.post(url, invalid_data_8, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_import_invalid_data_types_in_data(api_client):
    url = reverse("import_data")

    # Invalid data type: 'nazev_atributu' should be an integer (foreign key)
    invalid_data_1 = [
        {"attribute_name": {"nazev": "Barva"}},
        {"attribute_value": {"hodnota": "modrá"}},
        {
            "attribute": {"nazev_atributu": "not_an_int", "hodnota_atributu": 1}
        },  # 'nazev_atributu' should be an integer
    ]
    response = api_client.post(url, invalid_data_1, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data type: 'product' should be an integer (foreign key)
    invalid_data_2 = [
        {"product_attributes": {"product": "not_an_int", "attribute": 1}}
    ]  # 'product' should be an integer
    response = api_client.post(url, invalid_data_2, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data type: 'obrazek' should be a URL in Image
    invalid_data_3 = [
        {"image": {"obrazek": 789, "nazev": "Image Name"}}
    ]  # 'obrazek' should be a URL string
    response = api_client.post(url, invalid_data_3, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data type: 'product' should be an integer (foreign key) in ProductImage
    invalid_data_4 = [
        {
            "product_image": {
                "product": "not_an_int",
                "obrazek": 1,
                "nazev": "Main Photo",
            }
        }
    ]  # 'product' should be an integer
    response = api_client.post(url, invalid_data_4, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Invalid data type: 'nazev' should be a string in Catalog
    invalid_data_5 = [
        {
            "catalog": {
                "nazev": False,  # 'nazev' should be a string
                "obrazek": 1,
                "products_ids": [1, 2, 3],
                "attributes_ids": [1, 2, 3],
            }
        }
    ]
    response = api_client.post(url, invalid_data_5, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_model_detail(api_client, attribute_name):
    url = reverse("model_detail", args=["attribute_name", attribute_name.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["nazev"] == attribute_name.nazev


@pytest.mark.django_db
def test_product_detail(api_client, product):
    url = reverse("model_detail", args=["product", product.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["nazev"] == product.nazev


@pytest.mark.django_db
def test_catalog_detail(api_client, catalog):
    url = reverse("model_detail", args=["catalog", catalog.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["nazev"] == catalog.nazev
