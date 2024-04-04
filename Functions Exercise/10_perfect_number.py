def is_perfect_number(number):
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisors_sum == number

# Example usage:
number = int(input("Enter the number: "))
if is_perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
