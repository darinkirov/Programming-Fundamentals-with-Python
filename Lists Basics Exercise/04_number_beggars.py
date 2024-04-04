def distribute_offers(offers_str, beggars):
    offers = list(map(int, offers_str.split(', ')))
    sums = [0] * beggars

    for i in range(len(offers)):
        sums[i % beggars] += offers[i]

    return sums


# Taking input for the offers and the count of beggars
offers_str = input("Enter the offers separated by comma and space: ")
beggars = int(input("Enter the count of beggars: "))

# Distributing offers among beggars
result = distribute_offers(offers_str, beggars)

# Printing the sums each beggar brings home
print("Sums each beggar brings home:", result)
