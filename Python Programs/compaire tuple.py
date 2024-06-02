"""

                                CPM() REMOVE FROM PYTHON3

"""

#Declare tuple

tup1=(10,20,30,40)
tup2=(50,60,70,80)

#compaire tuples by cmp()
# First example
flag=cmp(tup1, tup2)

if flag==0:
    print("\n Tuple are same")
else:
    print("\n Tuple are not same")
    
# Second example

tup3=10,20,30,40

flag=cmp(tup1, tup3)

if flag==0:
    print("\n Tuple are same")
else:
    print("\n Tuple are not same")
    