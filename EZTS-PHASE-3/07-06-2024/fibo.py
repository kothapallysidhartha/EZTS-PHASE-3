# fibv=[0,1]
# def fib(n):
#     if n<0:
#         print("Incorrect input")
#     elif n<len(fibv):
#         return fibv[n]
#     fibv.append(fib(n-1)+fib(n-2))
#     return fibv[n]
# print(fib(int(input())))

# l=list(input().split(" "))
# print(l)



# li = [15,3,6,12,8,5]
# res=0
# def summ(li, res=0):
#     if li:
#         res += li[0]
#         #print("s")
#         return summ(li[1:], res)
#     else:
#         return res
# 
# print(summ(li))

# s = input()
# 
# def pal(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return pal(s[1:-1])
# 
# print("True" if pal(s) else "False")



# s = int(input())
# l = 10 ** (len(str(s)) - 1)
# 
# def pal(s, l):
#     if s <= 9:
#         return True
#     if s // l != s % 10:
#         return False
#     else:
#         s = (s % l) // 10
#         return pal(s, l // 100)
# 
# print("True" if pal(s, l) else "False")

a=int(input())
b=int(input())

a=b+a
b=a-b
a=a-b

print(a,b)