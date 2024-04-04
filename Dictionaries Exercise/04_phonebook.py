def main():
    phonebook = {}

    while True:
        entry = input()
        if entry == "search":
            break
        name, number = entry.split(" - ")
        phonebook[name] = number

    search_name = input()
    if search_name in phonebook:
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")

if __name__ == "__main__":
    main()
