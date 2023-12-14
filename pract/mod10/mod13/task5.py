import requests
BASE_URL = 'https://fakestoreapi.com'


def add_user():
    user_data = {
        "name": {
            'firstname': 'severus',
            'lastname': 'snape'
        }
    }

    response = requests.post(f'{BASE_URL}/users', json=user_data)
    print(response.json()['id'])


add_user()
