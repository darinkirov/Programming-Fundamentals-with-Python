def main():
    course_info = input().split(":")
    course_students = []

    while True:
        student_info = input()
        if student_info == course_info[2]:
            break
        name, ID, course = student_info.split(":")
        if course == course_info[2]:
            course_students.append((name, ID))

    for student in course_students:
        print(f"{student[0]} - {student[1]}")

if __name__ == "__main__":
    main()
