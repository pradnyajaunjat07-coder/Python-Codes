# Define two lists of numbers
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

# Use map and lambda to add corresponding elements
result = map(lambda x, y: x + y, list1, list2)

# Convert the map object to a list and print it
print(list(result))
