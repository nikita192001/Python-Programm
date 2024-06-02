#6.extend method
list1=[1,2,3,4]

list2=[5,6,7,8]

print("\n\n List 1 is ",list1)
print("\n\n List 2 is ",list2)

list1.extend(list2)

print("\n\n After extenting list2 to the list1 : ")
print("\n\n List 1 is ",list1)
# 7. pop method

#pop the last element of list
list1.pop() 
print("\n\n No index number List 1 is ",list1)

#pop the 0'th index element of list
list1.pop(0) 
print("\n\n Pop 0th index element then List1 is ",list1)

#pop the 4'th index element of list and return it
x=list1.pop(4)
print("\n\n Pop 4th index of list and return it ",x)

# 8. remove method
list2.remove(5)# value to parameter is most important
print("\n\n removing element 5 list 2 is ",list2)

# 9. Reverse method
list3=[1,2,3,4,5,6,7]
print("\n\n List 3 is ",list3)
list3.reverse()
print("\n\n  after reversing the List 3 is ",list3)


#10. __len__() method
n=list3.__len__()
print("\n\n  length of list3 is",n)

