import grading_utils

name = input("Enter student name: ")

mark1 = float(input("Enter mark 1: "))
mark2 = float(input("Enter mark 2: "))
mark3 = float(input("Enter mark 3: "))

marks = [mark1, mark2, mark3]

average = grading_utils.calculate_average(marks)
result = grading_utils.classify_result(average)

print("----- STUDENT REPORT -----")
print("Name:", name)
print("Marks:", marks)
print("Average:", average)
print("Result:", result)
