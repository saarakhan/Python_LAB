# to find reverse of a given number
n = int(input("Enter a number : "))

reverseN = 0
while n!= 0:
    # 3 steps
    digit = n % 10
    reverseN = reverseN * 10 + digit
    n //= 10

print(reverseN)

# 2nd method slicing
print(str(1234)[::-1])

