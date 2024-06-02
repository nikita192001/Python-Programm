#largest number between the three number

print("\n Enter the value for three numbers A ,B and C :")
A=int (input("\n A= "))
B=int (input("\n B = "))
C=int (input("\n C = "))

if A>B and A>C :
    print ("\n A is largest number ")
    
if B>A and B>C :
    print ("\n B is largest number ")
    
if C>A and C>B :
    print ("\n C is largest number ")
    
if A==B==C:
    print("\n Numbers are same")