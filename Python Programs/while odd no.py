#write a programe to display even numbers from 1 to n and display there sum

print("\n Enter a number to which you want a odd numbers", end=' ')
n=int(input())
print("\nThe number to which you want a odd numbers is : ",n)

i=1
sum=0
while i<=n :
    if i%2!=0 :
        print(i)
        sum=sum+i
        
    i+=1    
print("\n\n Sum of number is :",sum)