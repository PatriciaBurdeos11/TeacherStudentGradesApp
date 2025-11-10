students = {
    "s1": {"name": "Patt", "grades": {}},
    "s2": {"name": "Maricar", "grades": {}}
}

teachers = {
    "t1": {"name": "Mr. Mariane", "subject": "Math"}
}

def assign_grade(teacher_id, student_id, grade):
    subject = teachers[teacher_id]["subject"]
    students[student_id]["grades"][subject] = grade
    print(f"{teachers[teacher_id]['name']} assigned {grade} in {subject} to {students[student_id]['name']}.")

def view_grades(student_id):
    print(f"Grades for {students[student_id]['name']}:")
    for subject, grade in students[student_id]["grades"].items():
        print(f"{subject}: {grade}")

# Example usage
assign_grade("t1", "s1", 95)
assign_grade("t1", "s2", 88)

view_grades("s1")
view_grades("s2")
