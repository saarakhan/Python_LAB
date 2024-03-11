# to check whether given number a palindrome or not
# ex: 121 1001

# if number and its reverse is same
originalN = int(input("Enter a number :"))
temp = originalN
rev = 0
while originalN != 0:
    digit = originalN % 10
    rev = rev * 10 + digit
    originalN //= 10

if(temp == rev):
    print(temp, "is palindrome")
else:
    print(temp, "not a palindrome")
