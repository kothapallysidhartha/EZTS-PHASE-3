# d={}
# s = "cabbbac"
# me=0
# mo=-1
# for i in s:
#     if i not in d.keys():
#         d[i]=1
#     elif i in d.keys():
#         d[i]+=1
# for i in s:
#     if d[i]%2==0:
#         me+=d[i]
#         d[i]=0
#         print(d[i],"e")
#     elif d[i]%2!=0:
#         mo+=d[i]
#         d[i]=0
#         print(d[i],"o")
# 
# 
# print(mo+me)
# #return mo+me


n=int(input())
c=1
s=0
for i in range(0,n+1):
    if s==n:
        c+=1
        s=0
    elif s<n:
        s+=s+1
        print(s)
        continue
print(c)