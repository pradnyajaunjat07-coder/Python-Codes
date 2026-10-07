#Take an integer no from user input and reverse it using recursion.

def reverse_number(n, rev=0):
    if n == 0:
        return rev

    digit = n % 10
    rev = rev * 10 + digit

    return reverse_number(n // 10, rev)


num = int(input("Enter a number: "))

result = reverse_number(num)

print("Reverse =", result)
