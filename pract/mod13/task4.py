import requests
BASE_URL = 'https://fakestoreapi.com'


def get_users():
    response = requests.get(f"{BASE_URL}/users")
    print(response.json())


get_users()
