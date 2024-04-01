import math

def calculate_coins(group_size, days):
    coins = 0
    companions = group_size

    for day in range(1, days + 1):
        coins += 50 - 2 * companions

        if day % 3 == 0:
            coins -= 3 * companions

        if day % 5 == 0:
            coins += 20 * companions
            if day % 3 == 0:
                coins -= 2 * companions

        if day % 10 == 0:
            companions -= 2

        if day % 15 == 0:
            companions += 5

    coins_per_companion = math.floor(coins / group_size)
    return companions, coins_per_companion

def main():
    group_size = int(input("Enter the group size: "))
    days = int(input("Enter the number of days: "))

    companions_count, coins_per_companion = calculate_coins(group_size, days)
    print(f"{companions_count} companions received {coins_per_companion} coins each.")

if __name__ == "__main__":
    main()
