# to illustrate all logical and relational operator
#! Logical -> AND OR NOT
#! Relational  > >= < <= == !-

x = 5
y = 10

# "and" returns true when both condition are true 
if(x >= 5 and y <= 10):
    print("true")
else: 
    print("false")

# "or" returns true if any condition is true
if(x == 5 or y != 12):
    print("true")
else:
    print("false")

# "not" true-> false, false-> true
if(not(x > 5)):
    print("x is smaller than 5")
else:
    print("x is greater than 5")

#output 
'''
true
true
x is smaller than 5
'''
