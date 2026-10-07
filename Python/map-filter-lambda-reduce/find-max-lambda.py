# find max numbers using lambda.

def find_max():
    
    get_max = lambda x, y: x if x > y else y
    print(get_max(10, 20))

# Call the function.
find_max()
