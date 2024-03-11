# SMALLEST AND LARGEST
Li = [1,2,3,4,5]
def big(Li):
   max = Li[0]
   for i in range(1,len(Li)):
        if(Li[i]>max):
             max = Li[i] 
   return max
print(big(Li))

def small(Li):
   min = Li[0]
   for i in range(1,len(Li)):
        if(Li[i]<min):
             min = Li[i] 
   return min
print(small(Li))