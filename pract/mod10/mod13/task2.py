import requests
BASE_URL = 'https://fakestoreapi.com'


def get_categories():
    response = requests.get(f'{BASE_URL}/products/categories')
    categories = response.json()

    for category in categories:
        print(category)


get_categories()
