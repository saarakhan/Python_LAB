# To add 2 matrix
def matrix(m,n):
     O=[]
     for rows in range(m):
         row=[]
         for cols in range(n):
             
             inp=int(input(f"enter mat {[rows]}{[cols]}"))
             row.append(inp)
         O.append(row)
     return O
def sum(A,B):
    print("sum of matrix is")
    result=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j]+B[i][j])
        result.append(row)
    return result
m=int(input("enter no of rows"))
n=int(input("enter no of cols"))
print("first matrix is:")
A=matrix(m,n)
print(A)
print("second matrix is:")
B=matrix(m,n)
print(B)

s=sum(A,B)
print(s)