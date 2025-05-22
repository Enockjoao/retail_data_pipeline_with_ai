from etl.extract import Extract, url_products, url_carts, url_users
from etl.transform import Transform
from etl.load import Load

def main():
    extract = Extract(url_products, url_carts, url_users)

    products_json = extract.extract_products()
    carts_json = extract.extract_carts()
    users_json = extract.extract_users()

    transform = Transform(extract)

    products = transform.transform_products(products_json)
    carts = transform.transform_carts(carts_json)
    users = transform.transform_users(users_json)

    load = Load()

    load.load_products(products)
    load.load_carts(carts)
    load.load_users(users)

    print("ETL executada com sucesso!")

if __name__ == "__main__":
    main()
