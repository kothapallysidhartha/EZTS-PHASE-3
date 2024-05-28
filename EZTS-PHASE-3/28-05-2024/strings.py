
# prime number
# 1

# x=int(input("Enter a number:"))
# count=1
# if x==1:
#     print("Not a prime number")
# elif(x==2):
#     print(x,"is a prime number")
# elif x>=2:
#     for i in range(2,int(x/2)):
#         if(x%i)==0:
#             print(x,"is ","Not a prime number")
#             count=0
#             break
# #         else:
# #             count=1
# if(count==1):
#     print(x,"is a prime number")

# # 2 T.C:O(1), O(n)
# for i in range(2,x):			# 3 insted of x use "(x//2)+1" for better time complexity	T.C: O(n/2)
#     if x%i==0:
#         print("not a prime")
#         break
# else:
#     print("prime")

# # 4		T.C:O(sqrt(n))
# for i in range(2,int(x**0.5)+1):
#     if x%i==0:
#         print("not a prime")
#         break
# else:
#     print("prime")

# n=int(input(""))
# f=0
# while n > 1:
#     if n % 6 == 0:
#         f+=1
#     n //= 6
# print(f)
# if f==6:
#     print("y")
# else:
#     print("n")
#

def num(x):
    print(x)
    if x!=1:
        x-=1
        num(x)
n=int(input())
num(n)
    