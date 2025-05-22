import requests

url_products = "https://fakestoreapi.com/products"
url_carts = "https://fakestoreapi.com/carts"
url_users = "https://fakestoreapi.com/users"

class Extract:
    def __init__(self, url_products, url_carts, url_users):
        self.url_products = url_products
        self.url_carts = url_carts
        self.url_users = url_users

    def extract_products(self):
        response = requests.get(self.url_products)
        return(response.json())

    def extract_carts(self):
        response = requests.get(self.url_carts)
        return(response.json())

    def extract_users(self):
        response = requests.get(self.url_users)
        return(response.json())


extract = Extract(url_products, url_carts, url_users)




