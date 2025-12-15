import numpy as np

try:
    # Read input file
    input_file = "students.txt"
    output_file = "results.txt"

    students = []

    with open(input_file, "r") as file:
        for line in file:
            reg_no, exam, coursework = line.strip().split(",")
            exam = float(exam)
            coursework = float(coursework)

            # Calculate overall mark (70% exam, 30% coursework)
            overall = exam * 0.7 + coursework * 0.3

            # Assign grade
            if overall >= 75:
                grade = "A"
            elif overall >= 60:
                grade = "B"
            elif overall >= 50:
                grade = "C"
            else:
                grade = "F"

            students.append((reg_no, exam, coursework, overall, grade))

    # Create NumPy structured array
    dtype = [('RegNo', 'U10'), ('Exam', 'f4'), ('Coursework', 'f4'),
             ('Overall', 'f4'), ('Grade', 'U2')]
    students_array = np.array(students, dtype=dtype)

    # Sort by overall marks
    students_array = np.sort(students_array, order='Overall')[::-1]

    # Write output file
    with open(output_file, "w") as file:
        for student in students_array:
            file.write(f"{student['RegNo']}, {student['Overall']:.2f}, {student['Grade']}\n")

    # Display grade statistics
    unique, counts = np.unique(students_array['Grade'], return_counts=True)
    print("Grade Statistics:")
    for grade, count in zip(unique, counts):
        print(f"{grade}: {count}")

except FileNotFoundError:
    print("Input file not found.")
except Exception as e:
    print("Error:", e)
