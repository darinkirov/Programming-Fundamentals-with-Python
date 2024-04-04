def find_smallest(num1, num2, num3):
    return min(num1, num2, num3)


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

smallest = find_smallest(number1, number2, number3)
print("The smallest number is:", smallest)
