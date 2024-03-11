# to find factorial of a given number

n = int(input("Enter a number : "))

# 5 = 5*4*3*2*1
def findFact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(findFact(n))

