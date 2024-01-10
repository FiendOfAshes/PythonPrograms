# Adding n-bit binary digits
# First step: converting binary to decimal
# base case: if n is 0 return 0
# var reminder = (n%10)*exp
# return reminder + decimal(n//10, exp*10)
def decimal(n, exp=1):
    if n == 0:
        return n
    remainder = n%10  # modulo 10 to store the last digit
    remainder = remainder*exp  #multiply by exp to update
    return remainder + decimal(n//10, exp*2)
# add this

# print(decimal(1101,))
# Second step: converting decimal to binary
def binary(x):
    if x == 0:
        return str(x)
    return x%2 + 10*int((binary(x//2)))

# print(binary(13))

# Finally, to add to n-bit numbers
def add_binary(a, b):
    A = "".join([str(x) for x in a])
    B = "".join([str(x) for x in b])
    return binary(decimal(int(A)) + decimal(int(B)))

print(add_binary([1, 0, 1], [1, 1, 0, 1]))
