def calculate_ascii_sum(N):
    total_sum = 0
    for _ in range(N):
        character = input().strip()
        total_sum += ord(character)
    return total_sum

def main():
    N = int(input("Enter the number of characters: "))
    total_sum = calculate_ascii_sum(N)
    print(f"The sum equals: {total_sum}")

if __name__ == "__main__":
    main()
