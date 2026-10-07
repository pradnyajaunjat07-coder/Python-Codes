
# 1. Define the function with distinct names for variables
def display_student_info(name, *marks, **details):
    print("Name:", name)
    print("Marks (Tuple):", marks)
    print("Details (Dictionary):", details)

# 2. Call the function correctly outside of its definition
display_student_info("pradnya", 80, 75, 90, 95, age=24, city="Pune")
