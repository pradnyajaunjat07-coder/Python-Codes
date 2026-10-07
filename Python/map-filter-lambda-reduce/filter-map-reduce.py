#find even numbers square them then perform addition of only even numbers square.

from functools import reduce
# Define the initial list
numbers = [10, 8, 5, 7, 3] # here 10 and 8 are even numbers.

# 1. Filter out only the even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# 2. Square the filtered even numbers using map
even_squares = map(lambda x: x ** 2, even_numbers)

#3. Addition of even numbers squares using reduce function.
add_squares = reduce (lambda x,y : x+y, even_squares)

# Convert the final map object to a list and print it
print(add_squares)
