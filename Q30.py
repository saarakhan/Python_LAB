# To check whether a list is sorted or not
def is_sorted(lst):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            return  False
    return True

lst1=[15,6,8,9]
if is_sorted(lst1):
   print("list is sorted")
else:
   print("list is not sorted")

