# Write a function using **kwargs that prints only the values.

def print_values(**kwargs):
    # Loop through and print each value in the dictionary
    for value in kwargs.values():
        print(value)  # Fixed: Use print() to display the value

# Fixed: Moved the call outside the function so it executes properly
print_values(name="lily", age=19, city="Pune")
