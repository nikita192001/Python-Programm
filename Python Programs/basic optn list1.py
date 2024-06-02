#declare list
#1.append method

list1=[23,45,43,45,65,71,11,12,23,0]

print("\n\n The given list is : ",list1)
list1.append(450)
list1.append(22)

print("\n affter append operation the list is : ",list1)

# 2.copy method
list2=list1.copy()

print("\n\n Copy the list1 to list2 : ",list2)

#3.count method
print("\n\n how many times 45 in list1 is : ",list1.count(45)," times")

#4.insert method
list1.insert(2,1)

print("\n\n After inserting element 1 at index number 2 the list is : ",list1)

#5.clear() method
list1.clear()
print("\n\n After clearing the list1 is : ",list1)










