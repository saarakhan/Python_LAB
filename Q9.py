# To find sum of digits of a given number
number = (input("Enter number : "))
# 543 = 12 (5 + 4 + 3)
# 139 = 13 (1 + 3 + 9)
n = 0
for i in number:
    n = n + int(i) 

print(n)

