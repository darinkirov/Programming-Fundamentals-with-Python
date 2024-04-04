def calculate_total_price(product, quantity):
    prices = {
        "coffee": 1.50,
        "water": 1.00,
        "coke": 1.40,
        "snacks": 2.00
    }

    if product in prices:
        return prices[product] * quantity
    else:
        return "Invalid product"


# Example usage:
product = input("Enter the product (coffee, water, coke, snacks): ")
quantity = int(input("Enter the quantity: "))

total_price = calculate_total_price(product, quantity)
print(total_price)
