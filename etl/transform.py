from .extract import Extract, url_products, url_carts, url_users
import logging

class Transform:
    def __init__(self, extract):
        self.extract = extract

    def transform_products(self, products_json):
        try:
            transformed = []
            for product in products_json:
                transformed.append({
                    "id": product["id"],
                    "title": product["title"],
                    "price": product["price"],
                    "description": product["description"],
                    "category": product["category"]
                })
            logging.info("Products successfully transformed.")
            return transformed
        except Exception as e:
            logging.error(f"Failed to transform products: {e}")
            raise

    def transform_carts(self, carts_json):
        try:
            transformed = []
            for cart in carts_json:
                transformed.append({
                    "id": cart["id"],
                    "userId": cart["userId"],
                    "date": cart["date"],
                    "products": cart["products"]
                })
            logging.info("Carts successfully transformed.")
            return transformed
        except Exception as e:
            logging.error(f"Failed to transform carts: {e}")
            raise

    def transform_users(self, users_json):
        try:
            transformed = []
            for user in users_json:
                name = f"{user['name']['firstname']} {user['name']['lastname']}"
                transformed.append({
                    "id": user["id"],
                    "name": name,
                    "email": user["email"],
                    "address": user["address"],
                    "city": user["address"]["city"],
                    "number": user["address"]["number"]
                })
            logging.info("Users successfully transformed.")
            return transformed
        except Exception as e:
            logging.error(f"Failed to transform users: {e}")
            raise
