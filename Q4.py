# To find given number is even or odd
number = int(input("Enter the number : "))

def isEvenOdd(num):
    if(num % 2 == 0):
        print(num, "is even")
    else:
        print(num, "is odd")

isEvenOdd(number)

#output
'''
Enter the number : 10
10 is even

Enter the number : 13
13 is odd
'''