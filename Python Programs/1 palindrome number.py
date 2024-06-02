#palindrome number program

print("\n\n The number is palindrome or not")
n=int(input("\nEnter The Number :"))
reverse=0
original=n

if n>0:
    while n!=0 :
        remainder=n%10
        reverse=reverse*10+remainder
        n//=10 #Note floar and float division operator
        
    if original==reverse :
        print(n ,"\n The number is palindrome number")
    else :
        print(n ,"\n The number is NOT palindrome number")
        
else :
    print ("\n The number must be positive")