#nested list in python

list=[10,20,[2,3],34,["a","b"]]

print("\n Accessing individual elements")

print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[2][1])
print(list[4][0])

#display nested list  by using loop

print("\n using loop")
for i in list:
    print(i)