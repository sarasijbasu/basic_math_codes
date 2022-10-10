def palindrome(n):
    n_copy = n
    rev = 0
    while(n!=0):
        rev = rev*10 + n%10
        n = int(n/10)
    if n_copy == rev:
        return True
    else:
        return False