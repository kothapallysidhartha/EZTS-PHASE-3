
tcase=int(input())
tsum=0
for i in range(tcase):
    days,p,q,r=list(map(int,input().split()))
    for i in range(1,days+1):
        a=i%p
        b=i%q
        c=i%r
        if a==0 or b==0 or c==0:
            if a==0 and b==0:
                continue
            elif a==0 and c==0:
                continue
            elif b==0 and c==0:
                continue
            tsum+=1
    print(tsum)