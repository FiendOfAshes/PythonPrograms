def isPalindrome(x):
    y = str(x)
    if len(y) <= 1:  # base case
        return True
    else:
        if y[0] != y[-1]:
            return False
    return isPalindrome(y[1:-1])
