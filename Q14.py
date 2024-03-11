# Python program to check if the number is an Armstrong number or not

#! given number is Armstrong or not
# a number that is equal to sum of its digit, each raised to a power
# ex: 153 = (1)3 + (5)3 + (3)3
# ex: 1634 = (1)4 + (6)4 + (3)4 + (4)4

num = 1634

# calculated the length (number of digits)
order = len(str(num))

sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
