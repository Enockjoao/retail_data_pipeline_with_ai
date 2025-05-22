from .extract import Extract, url_products, url_carts, url_users

class Transform:
    def __init__(self, extract):
        self.extract = extract

    def transform_products(self, products_json):
        products_transformed = []
        for product in products_json:
            id = product["id"]
            title = product["title"]
            price = product["price"]
            description = product["description"]
            category = product["category"]
            products_transformed.append({
                "id": id,
                "title": title,
                "price": price,
                "description": description,
                "category": category,
            })
        return products_transformed

    def transform_carts(self, carts_json):
        carts_transformed = []
        for cart in carts_json:
            id = cart["id"]
            userId = cart["userId"]
            date = cart["date"]
            products = cart["products"]  
            carts_transformed.append({
                "id": id,
                "userId": userId,
                "date": date,
                "products": products
            })
        return carts_transformed

    def transform_users(self, users_json):
        users_transformed = []
        for user in users_json:
            id = user["id"]
            name = user["name"]["firstname"] + " " + user["name"]["lastname"]
            email = user["email"]
            address = user["address"]
            city = address["city"]
            number = address["number"]
            users_transformed.append({
                "id": id,
                "name": name,
                "email": email,
                "address": address,
                "city": city,
                "number": number
            })
        return users_transformed

if __name__ == "__main__":
    extract_instance = Extract(url_products, url_carts, url_users)
    products_json = extract_instance.extract_products()
    transform_instance = Transform(extract_instance)
    products_transformed = transform_instance.transform_products(products_json)
    print(products_transformed)
