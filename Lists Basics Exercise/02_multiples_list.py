def generate_multiples(factor, count):
    multiples = []
    current_multiple = factor

    for _ in range(count):
        multiples.append(current_multiple)
        current_multiple += factor

    return multiples

# Taking input for the factor and count
factor = int(input("Enter the factor: "))
count = int(input("Enter the count: "))

# Generating the list of multiples
multiples_list = generate_multiples(factor, count)

# Printing the list of multiples
print("List of multiples:", multiples_list)
