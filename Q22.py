#To create a list by concatenating a given list with a range from 1 to n
l1=['p','q','c']
l2=[]
n=int(input("enter value of n : "))

for i in range(1,n+1):
    for j in l1:
        l2.append(j+str(i))
print(l2)