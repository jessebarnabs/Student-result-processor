import grading_utils

marks = [55, 68, 72, 90, 61]

average = grading_utils.calculate_average(marks)
result = grading_utils.classify_result(average)

print("Module Average:", average)
print("Module Result:", result)