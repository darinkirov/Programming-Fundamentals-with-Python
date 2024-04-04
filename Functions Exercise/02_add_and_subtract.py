def sum_numbers(num1, num2):
    return num1 + num2

def subtract(result, num3):
    return result - num3

def add_and_subtract(num1, num2, num3):
    result = sum_numbers(num1, num2)
    return subtract(result, num3)

# Example usage:
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

result = add_and_subtract(number1, number2, number3)
print("The result of subtraction is:", result)
