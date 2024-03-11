# to remove dupicates from a list
Li = [1,2,3,4,5,1,3,5]    
Lis = []
[Lis.append(x) for x  in Li if x not in Lis]
print(Lis)