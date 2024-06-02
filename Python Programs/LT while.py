#Iterate list and tuple using while loop

print("\n Iterate list using while loop")
list=[1,2,3,4,5,6,7,8,9]

i=0

while i<list.__len__():
    print("\n element at index ",i,"is",list[i])
    i=i+1
 
# tuple
print("\n Iterate tuple using while loop")
tup=(1,2,3,4,5,6,7,8,9)

i=0

while i<tup.__len__():
    print("\n element at index ",i,"is",tup[i])
    i=i+1