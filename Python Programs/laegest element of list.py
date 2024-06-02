
list=[1,23,45,32,65,43,67,89,76,0]

#sort the element in assending order
list.sort()

#find largest element in list by negative indexing
print("\n\n Largest element of list is ", list[-1])

#find largest element in list by positive indexing
#first sort the list and then find its length
x=list.__len__()
print("\n\n Largest element of list is ",list[x-1])

