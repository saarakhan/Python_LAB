# using recursion , write python script for

# a>. printing binary number for a decimal number

def DecToBin(num): 
     if (num == 0):
          return 0
     else:
          return (num %2 + 10*DecToBin(int(num//2)))
print(DecToBin(7))


# b>. printing octal number for a decimal number
def DecToOctel(num): 
     if (num == 0):
          return 0
     else:
          return (num %8 + 10*DecToOctel(int(num//8)))
print(DecToOctel(13))

# c>. printing factorial of a number

def factorial(num):
     
    if(num == 0):
        return  1
    return  num*factorial(num-1)
print(factorial(5))
# c>. printing fibonnaci of a number

def Fibo(num):
   if(num == 1 or num == 2):
        return num-1
   return Fibo(num-1)+Fibo(num-2)
print(Fibo(5))

# e>. GEOMETRIC SUM
def geoSum(n):   
    if(n == 0 ):
        return 1
    return 1 / pow(3, n) + geoSum(n-1)
print(geoSum(5))

