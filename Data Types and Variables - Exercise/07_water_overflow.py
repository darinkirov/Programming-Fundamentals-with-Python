def pour_water(n, capacities):
    tank_capacity = 255
    total_liters = 0

    for _ in range(n):
        liters = int(input())
        if total_liters + liters > tank_capacity:
            print("Insufficient capacity!")
        else:
            total_liters += liters

    return total_liters

def main():
    n = int(input("Enter the number of lines: "))
    total_liters = pour_water(n, 255)
    print(total_liters)

if __name__ == "__main__":
    main()
