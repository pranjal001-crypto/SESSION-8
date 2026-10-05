def average(marks):
    return sum(marks) / len(marks)


def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 40:
        return "C"
    else:
        return "F"
