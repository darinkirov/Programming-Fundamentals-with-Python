import math

def calculate_courses_needed(N, P):
    return math.ceil(N / P)

def main():
    N = int(input("Enter the number of people: "))
    P = int(input("Enter the capacity of the elevator: "))

    courses_needed = calculate_courses_needed(N, P)
    print(f"Number of courses needed: {courses_needed}")

if __name__ == "__main__":
    main()
