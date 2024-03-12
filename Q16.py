# to print following pattern
'''
*
**
***
****
'''

n = int(input("Enter n: "))

print("--------Pattern-01----------")
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print("")

'''
****
***
**
*
'''
print("--------Pattern-02----------")

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print(" ")

print("--------Pattern-03----------")

'''
      *
    * * *
  * * * * *
'''

for i in range(n):
    for j in range(n,-1,-1):
        if  (i>=j):
            print('*',end=' ')
        else:
            print(' ',end='')
    print()
print("--------Pattern-04----------")

for i in range (1,5):
     for j in range(i):
          print(j+1,end=' ')
     print('')

print("--------Pascals Triangle----------")

def factorial(num):
     i = num
     if(num == 0):
          return  1
     fact =1
     while(i>0):
          fact *= i 
          i-=1
     return  fact

def nCr(n,r):
     return int ( factorial(n)/(factorial(r)*factorial(n-r)))

def pascal(limit):
    for i in range(limit):
        for  j in range(limit,-1,-1):
            if(i >=j):
                print(nCr(i,j),end=' ')
            else:
                print(" ",end='')
        print()     

pascal(n)

print("--------Floyd's Triangle----------")

counter =0
for i in range (n):
    for j in range(i+1):
        counter+=1
        print(counter,end=' ')
    print()


