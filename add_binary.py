# Adding n-bit binary digits
# First step: converting binary to decimal
# base case: if n is 0 return 0
# var reminder = (n%10)*exp
# return reminder + decimal(n//10, exp*10)
def decimal(n, exp=1):
    if n == 0:
        return n
    remainder = n%10  
    remainder = remainder*exp 
    return remainder + decimal(n//10, exp*2)

# Second step: converting decimal to binary
def binary(x):
    if x == 0:
        return str(x)
    return x%2 + 10*int((binary(x//2)))

# Finally, to add two n-bit binary integers in arrays
def add_binary(a, b):
    A = "".join([str(x) for x in a])
    B = "".join([str(x) for x in b])
    return binary(decimal(int(A)) + decimal(int(B)))

