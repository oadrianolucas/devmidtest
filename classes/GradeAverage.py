class GradeAverage:
    def calculate_average(grades):
        return sum(grades) / len(grades)

    def main():
        grades = []
        for subject in range(1, 4):
            grade = float(input(f"Enter the grade for subject {subject}: "))
            grades.append(grade)

        average = GradeAverage.calculate_average(grades)
        print(f"The average grade is: {average:.2f}")