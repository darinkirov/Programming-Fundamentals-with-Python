def main():
    resources = {}

    while True:
        resource = input()
        if resource == "stop":
            break
        quantity = int(input())

        if resource in resources:
            resources[resource] += quantity
        else:
            resources[resource] = quantity

    for resource, quantity in resources.items():
        print(f"{resource} -> {quantity}")

if __name__ == "__main__":
    main()
