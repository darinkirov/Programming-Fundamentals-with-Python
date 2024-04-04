def filter_numbers(category, numbers):
    if category == 'even':
        return [num for num in numbers if num % 2 == 0]
    elif category == 'odd':
        return [num for num in numbers if num % 2 != 0]
    elif category == 'negative':
        return [num for num in numbers if num < 0]
    elif category == 'positive':
        return [num for num in numbers if num >= 0]

# Taking input for the number of integers
n = int(input("Enter the number of integers: "))

# Taking input for the integers
numbers = [int(input()) for _ in range(n)]

# Taking input for the category
category = input("Enter the category (even, odd, negative, positive): ")

# Filtering the numbers based on the category
filtered_numbers = filter_numbers(category, numbers)

# Printing the filtered numbers
print("Filtered numbers:", filtered_numbers)
