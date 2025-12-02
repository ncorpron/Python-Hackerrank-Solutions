if __name__ == "__main__":
    students = []

    for _ in range(int(input())):
        name = input().strip()
        grade = float(input())
        students.append([name, grade])

    # Extract all grades
    grades = sorted({grade for _, grade in students})  # unique + sorted

    second_lowest = grades[1]  # second lowest grade

    # Get all names with that grade
    result = sorted([name for name, grade in students if grade == second_lowest])

    # Print names
    for name in result:
        print(name)

