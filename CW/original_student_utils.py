def average(marks):
    return sum(marks) / (len(marks) - 1)


def grade(mark):
    if mark >= 60:
        return "B"
    elif mark >= 90:
        return "A"
    elif mark >= 40:
        return "C"
    else:
        return "F"
