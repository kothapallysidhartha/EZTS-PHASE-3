
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


# def num(x):
#     print(x)
#     if x!=1:
#         x-=1
#         num(x)
# n=int(input())
# num(n)
#

import string

# strr = input()
# ne = ""
# for i in strr:
#     if i in string.digits:
#         ne += i
# print(int(ne))

# s=input()
# l=""+s[:1]
# for i in range(1,len(s)):
#     if s[i] != l[-1]:
#         l+=s[i]
# print(str(l))


data=input()
rot=int(input())
res=''
for i in range(rot):
    di,mag=input().split()
    if di.upper()=='L':
         res +=(data[int(mag):]+data[:int(mag)])[0]
    elif di.upper()=='R':
         res +=(data[:int(mag):]+data[int(mag)])[0]
sublist = [data[i:i+rot] for i in range(len(data))]        
for subele in sublist:
    if sorted(subele) == sorted(res):
        print('Yes')
        break
else:
     print('No')
