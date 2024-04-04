def is_palindrome(number):
    return str(number) == str(number)[::-1]

def check_palindromes(numbers):
    return [is_palindrome(num) for num in numbers]

numbers = input("Enter the list of positive integers separated by comma and space: ").split(", ")
results = check_palindromes(map(int, numbers))
print(results)
