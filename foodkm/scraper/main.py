from scrape_product_ids import get_all_ids
from scrape_products import get_product_info
from parse_product_info import extract_structured_product_info


def main():
    # Extract mercadona product ids (#try/except)
    df = get_all_ids()

    # Get the HTML content of each of the food products
    df['contenidos'] = get_product_info(df['product_id'].tolist())

    # Extract cleaned product info and save all the information
    extract_structured_product_info(df)


if __name__ == "__main__":
    main()
