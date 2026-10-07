#Multiplying each num into same number using map.

def square (x):
    return x*x

numbers = [1,2,3,4,5]

# Convert the map object into a standard list
result = list(map(square, numbers))

print(result)
