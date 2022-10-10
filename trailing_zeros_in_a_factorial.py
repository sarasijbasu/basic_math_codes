import math
def trailing_zero_effective(n):
    i = 5
    sum = 0
    while (math.floor(n/i) != 0):
        sum = sum + math.floor(n/i)
        i = i*5
    return(sum)
    
    
n = int(input("Enter the number n : "))
print(f"The trailing zeros for {n}! = {trailing_zero_effective(n)}")   