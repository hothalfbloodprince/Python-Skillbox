import requests
BASE_URL = 'https://fakestoreapi.com'


def get_jewelery():
    response = requests.get(f'{BASE_URL}/products')
    products = response.json()

    for product in products:
        if product['category'] == 'jewelery':
            print(product)


get_jewelery()
