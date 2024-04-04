def classify_numbers(n):
    positives = []
    negatives = []
    sum_of_negatives = 0

    for _ in range(n):
        num = int(input())
        if num >= 0:
            positives.append(num)
        else:
            negatives.append(num)
            sum_of_negatives += num

    count_positives = len(positives)

    return positives, negatives, count_positives, sum_of_negatives


# Taking input for the number of integers
n = int(input("Enter the number of integers: "))

# Creating the lists of positives and negatives
positives, negatives, count_positives, sum_of_negatives = classify_numbers(n)

# Printing the lists of positives and negatives
print("List of positives:", positives)
print("List of negatives:", negatives)

# Printing count of positives and sum of negatives
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")
