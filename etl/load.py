import json
import os
import logging
from tinydb import TinyDB

DATA_DIR = r"C:\Users\vitor\Desktop\api_with_ia\data"

class Load:
    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        self.db = TinyDB(os.path.join(DATA_DIR, 'tinydb.json'))

    def load_products(self, products):
        try:
            file_path = os.path.join(DATA_DIR, "products.json")
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(products, f, ensure_ascii=False, indent=4)
            self.db.table("products").insert_multiple(products)
            logging.info(f"Products successfully saved to {file_path} and TinyDB.")
        except Exception as e:
            logging.error(f"Failed to load products: {e}")
            raise

    def load_carts(self, carts):
        try:
            file_path = os.path.join(DATA_DIR, "carts.json")
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(carts, f, ensure_ascii=False, indent=4)
            self.db.table("carts").insert_multiple(carts)
            logging.info(f"Carts successfully saved to {file_path} and TinyDB.")
        except Exception as e:
            logging.error(f"Failed to load carts: {e}")
            raise

    def load_users(self, users):
        try:
            file_path = os.path.join(DATA_DIR, "users.json")
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(users, f, ensure_ascii=False, indent=4)
            self.db.table("users").insert_multiple(users)
            logging.info(f"Users successfully saved to {file_path} and TinyDB.")
        except Exception as e:
            logging.error(f"Failed to load users: {e}")
            raise
