'''Given a dictionary of products and their prices, find the product with the
highest price.'''
# Dictionary of products and prices
products = {
    "Laptop": 55000,
    "Mobile": 25000,
    "Tablet": 30000,
    "Headphones": 2000
}

# Find product with highest price
highest_price_product = max(products, key=products.get)

print("Product with highest price:", highest_price_product)
print("Price:", products[highest_price_product])
