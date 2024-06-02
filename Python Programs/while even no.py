#write a programe to display even numbers from 1 to n
print("\n Enter a number to which you want a even numbers", end=' ')
n=int(input())
print("\nThe number to which you want a even numbers is : ",n)

i=1
while i<=n :
    if i%2==0 :
        print(i)
        
    i+=1    
