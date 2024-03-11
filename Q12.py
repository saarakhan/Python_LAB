# To print Fibonacci series upto nth term
#  1 1 2 3 5 8 13 21
# curr_no = prev1 + prev2

n = int(input("Enter a number : "))
num1 = 0
num2 = 1
next_number = num2  
count = 1
 
while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2

#Recursion
# To print nth Fibonacci number
def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(9))