'''
                basic
                tuple
                function '''

#__add__()
tup1=12,23,2,0
print("\n tuple1 : ",tup1)

tup2=2,3,45,6,7
print("\n tuple2 : ",tup2)

tup3= tup1.__add__(tup2)

print("\n tuple3 : ",tup3)

#index()
x=tup1.index(0)

print("\n Index of element 0 is : ",x)

#max()
y=max(tup3)

print("\n Maximum number of tuple 3 is ",y)

# min()
z=min(tup3)
print("\n Minimum number of tuple 3 is ",z)
