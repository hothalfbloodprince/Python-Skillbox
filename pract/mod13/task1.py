import requests
BASE_URL = 'https://fakestoreapi.com'


def get_products():
    response = requests.get(f'{BASE_URL}/products')
    products = response.json()

    for product in products:
        if product['price'] < 20:
            print(product)


get_products()
