# Check whether a number is palindrome
# Concept used: Recursion

def reverse_number(n, rev=0):
    if n == 0:
        return rev

    digit = n % 10
    rev = rev * 10 + digit 

    return reverse_number(n // 10, rev)


n = int(input("Enter a number: "))

reverse = reverse_number(n)

if n == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")