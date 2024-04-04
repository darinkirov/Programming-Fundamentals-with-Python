def main():
    # Input the stock
    stock_input = input().split()
    stock = {}

    for i in range(0, len(stock_input), 2):
        product = stock_input[i]
        quantity = int(stock_input[i + 1])
        stock[product] = quantity

    products_to_search = input().split()

    for product in products_to_search:
        if product in stock:
            print(f"We have {stock[product]} of {product} left")
        else:
            print(f"Sorry, we don't have {product}")


if __name__ == "__main__":
    main()
