def opposite_numbers(numbers_str):
    numbers = list(map(int, numbers_str.split()))  # Convert the input string to a list of integers
    opposite_nums = [-num for num in numbers]     # Compute the opposite of each number
    return opposite_nums

# Taking input for the string containing numbers
numbers_str = input("Enter positive and negative numbers separated by a single space: ")

# Getting the list of opposite numbers
opposite_list = opposite_numbers(numbers_str)

# Printing the list of opposite numbers
print("Opposite numbers:", opposite_list)
