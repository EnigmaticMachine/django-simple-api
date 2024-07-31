#!/bin/bash

# Define the base URL
BASE_URL="http://localhost:8000"

# Define the endpoint URLs
IMPORT_URL="${BASE_URL}/import/"

# Define the data to be sent
DATA='[
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
            "published_on": null,
            "is_published": false
        }
    },
    {"image": {"obrazek": "https://free-images.com/or/4929/fridge_t_png.jpg"}},
    {
        "image": {
            "nazev": "plná lednice",
            "obrazek": "https://free-images.com/or/ccc6/faulty_fridge_lighting_led_0.jpg"
        }
    },
    {"product_image": {"product": 1, "obrazek": 1, "nazev": "hlavní foto"}},
    {
        "catalog": {
            "nazev": "Výprodej 2018",
            "obrazek": 2,
            "products_ids": [1],
            "attributes_ids": [1, 2, 3]
        }
    }
]'

# Function to send a POST request to import data
import_data() {
  echo "Importing data..."
  response=$(curl -s -o /dev/null -w "%{http_code}" -X POST $IMPORT_URL \
    -H "Content-Type: application/json" \
    -d "$DATA")

  if [ "$response" -eq 201 ]; then
    echo "Data imported successfully."
  else
    echo "Failed to import data. HTTP status code: $response"
    exit 1
  fi
}

# Function to verify the catalog data
verify_catalog() {
  echo "Verifying catalog..."
  response=$(curl -s "${BASE_URL}/detail/catalog/1/" -H "Content-Type: application/json")
  echo "Catalog response: $response"
}

# Function to verify the attribute data
verify_attribute() {
  echo "Verifying attribute..."
  response=$(curl -s "${BASE_URL}/detail/attribute/3/" -H "Content-Type: application/json")
  echo "Attribute response: $response"
}

# Function to verify the product data
verify_product() {
  echo "Verifying product..."
  response=$(curl -s "${BASE_URL}/detail/product/1/" -H "Content-Type: application/json")
  echo "Product response: $response"
}

# Run the import data function
import_data

# Run the verification functions
verify_catalog
verify_attribute
verify_product
