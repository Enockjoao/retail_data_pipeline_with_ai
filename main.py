import logging
from etl.extract import Extract, url_products, url_carts, url_users
from etl.transform import Transform
from etl.load import Load

# Setup logging
logging.basicConfig(
    filename='etl_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    logging.info("Starting ETL process...")

    try:
        extract = Extract(url_products, url_carts, url_users)
    except Exception as e:
        logging.error(f"Extract initialization failed: {e}")
        return

    try:
        products_data = extract.extract_products()
        carts_data = extract.extract_carts()
        users_data = extract.extract_users()
    except Exception as e:
        logging.error(f"Data extraction failed: {e}")
        return

    try:
        transform = Transform(extract)
        products = transform.transform_products(products_data)
        carts = transform.transform_carts(carts_data)
        users = transform.transform_users(users_data)
    except Exception as e:
        logging.error(f"Data transformation failed: {e}")
        return

    try:
        load = Load()
        load.load_products(products)
        load.load_carts(carts)
        load.load_users(users)
    except Exception as e:
        logging.error(f"Data loading failed: {e}")
        return

    logging.info("ETL process completed successfully.")

if __name__ == "__main__":
    main()
