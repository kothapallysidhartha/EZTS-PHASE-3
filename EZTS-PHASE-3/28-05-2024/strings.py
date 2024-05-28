# n=int(input(""))
x=int(input("Enter a number:"))
count=1
if x==1:
    print("Not a prime number")
elif(x==2):
    print(x,"is a prime number")
elif x>=2:
    for i in range(2,int(x/2)):
        if(x%i)==0:
            print(x,"is ","Not a prime number")
            count=0
            break
#         else:
#             count=1
if(count==1):
    print(x,"is a prime number")