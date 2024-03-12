# TO print tabel of '10' until users choice using the list comprehsion sum and labda fuction

#! List Comprehsion

n=int(input("enter a number : "))
num=int(input("enter upto where : "))
list=[f"{n} * {i} = {n*i}" for i in range(1,num+1)]
print("\n".join(list))

#! Lambda function

x=int(input("enter a number : "))
i=int(input("enter upto where : "))
list=map(lambda i:f"{x}*{i}={x*i}",range(1,i+1))
print("\n".join(list))