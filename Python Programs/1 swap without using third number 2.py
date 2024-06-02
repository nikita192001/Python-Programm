print(" Swap two numbers without using THIRD variable")

print("\nswap two numbers first method * and //")

x=int(input("\n Enter first number" ))
y=int(input("\n Enter second number"))

print("\n Before swaping of two numbers")  
print(" The first numbers is ", x ," and second number is ",y )

x=x*y
y=x//y
x=x*y

print("\n After swaping of two numbers")  
print(" The first numbers is ",x ," and second number is ",y )