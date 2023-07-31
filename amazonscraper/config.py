def get_search_term():
    search_term = input("Product: ").strip().lower()
    while search_term == "":
        search_term = input("Product: ").strip().lower()
    return search_term

def get_specific_brand():
    specific_brand = input("Do you want to search for a specific brand? (y/n): ").lower().strip()
    if specific_brand == "y":
        brand = input("Brand: ").lower().strip()
        while brand == "":
            brand = input("Brand: ").lower().strip()
        return brand
    return None

def get_price_range():
    min_price = None
    max_price = None
    if input("Do you want to set a price range? (y/n): ").lower().strip() == "y":
        min_price = float(input("Min price: ").strip())
        while min_price == "":
            min_price = float(input("Min price: ").strip())
        max_price = float(input("Max price: ").strip())
        while max_price == "":
            max_price = float(input("Max price: ").strip())
    return min_price, max_price