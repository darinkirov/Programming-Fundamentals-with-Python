def characters_in_between(char1, char2):
    result = ''
    start = min(ord(char1), ord(char2)) + 1
    end = max(ord(char1), ord(char2))

    for char_code in range(start, end):
        result += chr(char_code) + ' '

    return result.strip()



char1 = input("Enter the first character: ")
char2 = input("Enter the second character: ")

result = characters_in_between(char1, char2)
print("Characters in between:", result)
