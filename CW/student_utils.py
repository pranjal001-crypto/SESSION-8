def calculate_average(marks):
    return sum(marks) / len(marks)


def assign_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 40:
        return "C"
    return "F"
