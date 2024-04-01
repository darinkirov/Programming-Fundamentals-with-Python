def print_ascii_range(start_index, end_index):
    for char_code in range(start_index, end_index + 1):
        print(chr(char_code), end=" ")


def main():
    start_index = int(input("Enter the start index: "))
    end_index = int(input("Enter the end index: "))

    print_ascii_range(start_index, end_index)


if __name__ == "__main__":
    main()
