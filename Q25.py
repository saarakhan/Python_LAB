# to multiply 2 matrix
def matrix(m,n):
    output=[]
    for i in range(0,m):
        row=[]
        for j in range(0,n):
            inp=int(input(f"enter output{[i]}{[j]} :"))
            row.append(inp)
        output.append(row)   
    return output

def mul(A,B):
    if (len(A[0])!= len(B)):
        print("matrix multiplication is not allowed")
        exit(0)
    output=[]
    for i in range(row1):
        row=[]
        for j in range(col2):
            t=0
            for k in range(col1):
                t+=(A[i][k]*B[k][j])
            row.append(t)
        output.append(row)
    return output

   
row1=int(input("enter no of rows of first matrix"))
col1=int(input("enter no of columns of first matrix"))

A=matrix(row1,col1)
print(A)
row2=int(input("enter no of rows of second matrix"))
col2=int(input("enter no of columns of second matrix"))

B=matrix(row2,col2)
print(B)
x=mul(A,B)
print("multiplicaion of matrix")
print(x)

