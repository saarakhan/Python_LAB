# to find the given number is prime or composite
  
num = int(input("Enter a number : "))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is composite number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is composite number")