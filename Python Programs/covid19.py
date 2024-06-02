#WAP to accept age from user. if age of user is greater than equal to 18 then
# user is eligibe for vaccine otherwise not eligible.

print("\n Enter age of user : ", end=' ')

x=int(input())

if(x<0):
    print("\n Invalid age or age must be positive ")
    
if(x<18):
    print("\n User is not eligible for covid vaccine ")
    
if (x>=18):
    print("\n User is eligible for covid vaccine ")
    
    