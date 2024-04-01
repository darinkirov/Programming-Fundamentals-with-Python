def is_happy_year(year):
    year_str = str(year)
    return len(set(year_str)) == len(year_str)

def next_happy_year(current_year):
    next_year = current_year + 1
    while not is_happy_year(next_year):
        next_year += 1
    return next_year

def main():
    current_year = int(input("Enter the current year: "))
    next_happy = next_happy_year(current_year)
    print(f"The next happy year after {current_year} is: {next_happy}")

if __name__ == "__main__":
    main()
