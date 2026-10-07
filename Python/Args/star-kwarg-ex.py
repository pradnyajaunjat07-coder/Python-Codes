#In Python, **kwargs (short for "keyword arguments") is a special syntax used in a function definition
#to accept a variable number of named/keyword arguments

def print_user_info(**kwargs):
    # kwargs will capture the dictionary elements as individual keyword arguments
    print("User Data inside function:", kwargs)

# Define your dictionary outside
user_data = {'name': "pradnya", 'age': 20, 'city': "Pune"}

# Pass the dictionary into the function using **
print_user_info(**user_data)




