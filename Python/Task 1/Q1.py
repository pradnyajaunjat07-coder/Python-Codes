# Write a function using *args to find the largest number without using max.

def largest(*args):
    # Start by assuming the first number is the largest
    largest_num = args[0]

    for num in args:
        if num > largest_num:  # Fixed: Added missing colon
            largest_num = num

    return largest_num  # Fixed: Moved outside the for-loop

# Fixed: Added a comma between the string and the function call
print("Largest Number:", largest(10, 25, 7, 45, 32))
