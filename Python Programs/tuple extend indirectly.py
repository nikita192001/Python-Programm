#tuple is not mutable but there is a way we can extend it indirectly

tup=(10,20,30,40)

print("\n Element of tuple before change are : ",tup)

tup=tup+(50,"abc")

print("\n Element of tuple after change are : ",tup)