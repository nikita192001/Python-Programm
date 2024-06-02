#write a program to calculate the factorial of the given number
n=int(input("\n Calculate factorial of the number : "))
fact=1
i=1

while i<=n :
    fact=fact*i;
    i=i+1
    
print ("\n Factorial of given number is ",fact)
