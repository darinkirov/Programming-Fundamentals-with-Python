def grade_to_words(grade):
    if grade >= 2.00 and grade <= 2.99:
        return "Fail"
    elif grade >= 3.00 and grade <= 3.49:
        return "Poor"
    elif grade >= 3.50 and grade <= 4.49:
        return "Good"
    elif grade >= 4.50 and grade <= 5.49:
        return "Very Good"
    elif grade >= 5.50 and grade <= 6.00:
        return "Excellent"
    else:
        return "Invalid grade"


grade = float(input("Enter the grade (between 2.00 and 6.00): "))
print(grade_to_words(grade))
