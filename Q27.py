# To find all the numbers of a list that are divisble by a particular element
list=eval(input("enter a list"))
print("lsit entered is",list)
n=int(input("enter any element "))
l2=[]
for i in list:
    if(i%n==0):
        l2.append(i)
    else:
        pass
print("Number divisible by particular element is")
print(l2)