def sum_even_odd_digits(number):
    odd_sum = sum(int(digit) for digit in str(number) if int(digit) % 2 != 0)
    even_sum = sum(int(digit) for digit in str(number) if int(digit) % 2 == 0)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = int(input("Enter the number: "))

result = sum_even_odd_digits(number)
print(result)
