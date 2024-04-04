def create_course_list(n):
    courses = []
    for _ in range(n):
        course_name = input("Enter the name of the course: ")
        courses.append(course_name)
    return courses


# Taking input for the number of courses
n = int(input("Enter the number of courses: "))

# Creating the list of courses
course_list = create_course_list(n)

# Printing the list of courses
print("List of courses:")
for course in course_list:
    print(course)
