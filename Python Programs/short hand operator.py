#WAP to demonstrate short hand operator in if satement
# accept two numbers
A=int(input( "\n A = "))
B=int(input("\n B= "))
 
#find largest number
max = A if A>B else B;

print("\n Largest number is : ", max)

#Or method

print("\n A is largest number ", A) if A > B else print("\n B is largest number ", B)