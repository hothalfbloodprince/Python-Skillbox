import requests
BASE_URL = 'https://fakestoreapi.com'
response = requests.get(f"{BASE_URL}/products")
print(response.json())

new_product = {
    "title": 'new product',
    "price": 1984,
    "description": 'amazing',
    "category": 'electronic',
    "image": 'https://i.pravatar.cc'
}
response = requests.post(f"{BASE_URL}/products", json=new_product)
print(response.json())

response = requests.delete(f"{BASE_URL}/products/1")
print(response.json())
