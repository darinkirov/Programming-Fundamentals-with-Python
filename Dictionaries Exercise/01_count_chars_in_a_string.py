def count_characters(string):
    char_count = {}

    for char in string:

        if char != " ":
            char_count[char] = char_count.get(char, 0) + 1

    for char, count in char_count.items():
        print(f"{char} -> {count}")


sample_string = "Hello World"
count_characters(sample_string)
