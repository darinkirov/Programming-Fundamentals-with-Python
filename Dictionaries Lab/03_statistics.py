def main():
    products = {}

    while True:
        data = input()
        if data == "statistics":
            break

        product, quantity = data.split(": ")
        quantity = int(quantity)

        if product in products:
            products[product] += quantity
        else:
            products[product] = quantity

    print("Products in stock:")
    for product, quantity in products.items():
        print(f"- {product}: {quantity}")

    count_all_products = len(products)
    sum_all_quantities = sum(products.values())
    print(f"Total Products: {count_all_products}")
    print(f"Total Quantity: {sum_all_quantities}")


if __name__ == "__main__":
    main()
