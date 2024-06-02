print("Reverse Number Program")
n=int(input("Enter the number to be reverse "))
original=n
reverse=0
while n>0 :
    remainder=n%10
    reverse=(reverse*10 ) + remainder
    n//=10
    
print("\n Reverse of the number " , original , " is ",reverse)