def remove_smallest(numbers, n):
    sorted_numbers = sorted(numbers)
    remaining_numbers = sorted_numbers[n:]
    return remaining_numbers

numbers = list(map(int, input().split()))
n = int(input())

remaining_numbers = remove_smallest(numbers, n)

print(", ".join(map(str, remaining_numbers)))
