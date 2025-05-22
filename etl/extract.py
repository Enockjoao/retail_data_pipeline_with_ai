import requests
import logging

url_products = "https://fakestoreapi.com/products"
url_carts = "https://fakestoreapi.com/carts"
url_users = "https://fakestoreapi.com/users"

class Extract:
    def __init__(self, url_products, url_carts, url_users):
        self.url_products = url_products
        self.url_carts = url_carts
        self.url_users = url_users

    def extract_products(self):
        try:
            response = requests.get(self.url_products)
            response.raise_for_status()
            logging.info("Products successfully extracted.")
            return response.json()
        except Exception as e:
            logging.error(f"Failed to extract products: {e}")
            raise

    def extract_carts(self):
        try:
            response = requests.get(self.url_carts)
            response.raise_for_status()
            logging.info("Carts successfully extracted.")
            return response.json()
        except Exception as e:
            logging.error(f"Failed to extract carts: {e}")
            raise

    def extract_users(self):
        try:
            response = requests.get(self.url_users)
            response.raise_for_status()
            logging.info("Users successfully extracted.")
            return response.json()
        except Exception as e:
            logging.error(f"Failed to extract users: {e}")
            raise
