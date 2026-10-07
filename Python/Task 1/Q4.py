#Write a function using **kwargs to calculate the total marks.

def total_marks(**marks):
    total = 0

    for mark in marks.values():
        total = total + mark  # Fixed: Changed 'marks' to 'mark'

    print("Total Marks:", total)  # Fixed: Moved outside the loop to print once

# Fixed: Moved the function call outside the definition (left margin)
total_marks(python=80, Java=75, Math=90, DBMS=85)
