# To transpose a matrix
def inputm(row1,col1):
  output=[]
  for i in range(row1):
    row=[]
    for j in range(col1):
      inp=int(input(f"Enter output {[i]}{[j]}"))
      row.append(inp)
    output.append(row)
  return output

def transposem(A):
  result=[]
  for i in range(len(A[0])):
    row=[]
    for j in range(len(A)):
      row.append(A[j][i])
    result.append(row)
  return result

row1=int(input("enter no of rows of first matrix"))
col1=int(input("enter no of columns of first matrix"))


A=inputm(row1,col1)
print("inputed matrix is :")
print(A)

print("Transpose of matrix is :")
print(transposem(A))