# to print  all palindorms for a range 500-1000

def isPalindrome(originalN):
    temp = originalN
    rev = 0
    while originalN != 0:
        digit = originalN % 10
        rev = rev * 10 + digit
        originalN //= 10

    if(temp == rev):
        print(temp,"is palindrome")


for i in range(500, 1001):
    isPalindrome(i)