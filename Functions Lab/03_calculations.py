def calculate_result(operator, num1, num2):
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return num1 / num2
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2
    else:
        return "Invalid operator"


operator = input()
num1 = int(input())
num2 = int(input())

result = calculate_result(operator, num1, num2)
print(result)
