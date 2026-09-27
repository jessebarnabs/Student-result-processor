student_name = "James"
registration_number = "001"
age = 21
average_mark = 78.5
registered = True

print(student_name, type(student_name))
print(registration_number, type(registration_number))
print(age, type(age))
print(average_mark, type(average_mark))
print(registered, type(registered))

unit1 = 65
unit2 = 72
unit3 = 58

total = unit1 + unit2 + unit3
average = total / 3

print("Total:", total)
print("Average:", average)

passed = average >= 50 and unit1 >= 40 and unit2 >= 40 and unit3 >= 40
print("Passed:", passed)

if average >= 70:
    grade = "Distinction"
elif average >= 50:
    grade = "Pass"
else:
    grade = "Fail"

print("Grade:", grade)

marks = [55, 68, 72, 90, 61]

for mark in marks:
    print("Mark:", mark)

marks_total = sum(marks)
marks_average = marks_total / len(marks)

print("Marks Total:", marks_total)
print("Marks Average:", marks_average)

def calculate_average(marks):
    return sum(marks) / len(marks)

def classify_result(average):
    if average >= 70:
        return "Distinction"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"

func_average = calculate_average(marks)
func_result = classify_result(func_average)

print("Function Average:", func_average)
print("Function Result:", func_result)