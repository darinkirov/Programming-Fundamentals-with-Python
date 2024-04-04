def filter_strings_with_word(n, word, strings):
    # Add all strings to a list
    all_strings = strings

    # Filter out strings containing the given word
    filtered_strings = [string for string in all_strings if word in string]

    return all_strings, filtered_strings


# Taking input for the number of strings
n = int(input("Enter the number of strings: "))

# Taking input for the word
word = input("Enter the word to filter: ")

# Taking input for the strings
strings = [input() for _ in range(n)]

# Printing all strings
print("All strings:")
for string in strings:
    print(string)

# Filtering strings containing the word
all_strings, filtered_strings = filter_strings_with_word(n, word, strings)

# Printing filtered strings
print("\nFiltered strings containing the word '{}':".format(word))
for string in filtered_strings:
    print(string)
