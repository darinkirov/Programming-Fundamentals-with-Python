def main():
    stock_input = input().split()
    stock = {}


    for i in range(0, len(stock_input), 2):
        key = stock_input[i]
        value = int(stock_input[i + 1])
        stock[key] = value

    print(stock)

if __name__ == "__main__":
    main()
