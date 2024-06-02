print("\n The number is armstrong or not",end='')
n=int(input ("\n Enter the number : "))
sum=0
original=n

while n>0 :
    remainder=n%10
    sum=sum+(remainder*remainder*remainder)
    n//=10
    
if(original==sum):
    print("\n The number is armstrong number ")
    
else :
    print("\n Number is not armstrong number")
    
    # for eg 153  370 371  407
    # armstrong no is no in all digit cube sum is equal to original number
