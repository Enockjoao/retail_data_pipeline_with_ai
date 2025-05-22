import os
import json
from tinydb import TinyDB, Query

# Set the base path where to save the JSON files and TinyDB
BASE_PATH = r"C:\Users\vitor\Desktop\api_with_ia\data"
os.makedirs(BASE_PATH, exist_ok=True)  

# Paths to JSON and TinyDB files
PRODUCTS_JSON_PATH = os.path.join(BASE_PATH, "products.json")
CARTS_JSON_PATH = os.path.join(BASE_PATH, "carts.json")
USERS_JSON_PATH = os.path.join(BASE_PATH, "users.json")
TINYDB_PATH = os.path.join(BASE_PATH, "database.json")

class Load:
    def __init__(self):
        # Initialize the TinyDB database
        self.db = TinyDB(TINYDB_PATH)
        # Create separate tables in TinyDB for products, carts and users
        self.products_table = self.db.table('products')
        self.carts_table = self.db.table('carts')
        self.users_table = self.db.table('users')

    def save_json(self, data, filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_products(self, products):
        # Save to JSON file
        self.save_json(products, PRODUCTS_JSON_PATH)

        # Saves to TinyDB - updates if id already exists, otherwise inserts
        for product in products:
            # Query object to search for the product by id
            Product = Query()
            if self.products_table.contains(Product.id == product['id']):
                self.products_table.update(product, Product.id == product['id'])
            else:
                self.products_table.insert(product)

    def load_carts(self, carts):
        self.save_json(carts, CARTS_JSON_PATH)

        Cart = Query()
        for cart in carts:
            if self.carts_table.contains(Cart.id == cart['id']):
                self.carts_table.update(cart, Cart.id == cart['id'])
            else:
                self.carts_table.insert(cart)

    def load_users(self, users):
        self.save_json(users, USERS_JSON_PATH)

        User = Query()
        for user in users:
            if self.users_table.contains(User.id == user['id']):
                self.users_table.update(user, User.id == user['id'])
            else:
                self.users_table.insert(user)


if __name__ == "__main__":
    # Exemple the usage with your extract and transform modules
    from extract import Extract, url_products, url_carts, url_users
    from transform import Transform

    extract = Extract(url_products, url_carts, url_users)
    transform = Transform(extract)

    # Extract Data
    products_json = extract.extract_products()
    carts_json = extract.extract_carts()
    users_json = extract.extract_users()

    # Transform Data
    products = transform.transform_products(products_json)
    carts = transform.transform_carts(carts_json)
    users = transform.transform_users(users_json)

    # Load Data
    load = Load()
    load.load_products(products)
    load.load_carts(carts)
    load.load_users(users)

    print("Data loaded successfully!")
