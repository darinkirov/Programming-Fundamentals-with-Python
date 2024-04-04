repeat_string = lambda s, n: s * n


input_string = input("Enter a string: ")
n = int(input("Enter the number of times to repeat the string: "))

result = repeat_string(input_string, n)
print(result)
