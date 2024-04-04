def main():
    # Input the list of characters
    characters = input().split(", ")

    # Create a dictionary using dictionary comprehension
    ascii_dict = {char: ord(char) for char in characters}

    # Print the dictionary
    print(ascii_dict)

if __name__ == "__main__":
    main()
