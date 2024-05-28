"""l1=list(map(int,input().split(" ")))
l2=list(map(int,input().split(" ")))
l1=l1+l2
l1.sort()
print(l1)"""

#lexicograhical number

"""j = int(input(""))
li = []
for i in range(1, j+1):
    li.append(str(i))
li.sort()
print(list(map(int,li)))
"""

"""
li=list(map(str,input().split(" ")))
li[-1],li[0]=li[0],li[-1]
print(li)
"""

"""
li=list(map(int,input().split()))
max_num = max(li)
k=len(li)
l=int(len(li)/2)
res=0
all(element == 0 for element in li)
while k or not all:
    max_num = max(li)
    l=li.index(max_num)-1
    r=li.index(max_num)+1
    if li.index(max_num)==0 and li[r]<max_num:
        res+=max_num
        li[r],li[l+1]=0,0
    elif li.index(max_num)==k-1 and li[l]<max_num:
        res+=max_num
        li[l],li[l+1]=0,0
    elif (r<k and l>-1) and li[l]+li[r]>max_num:
        res+=(li[l]+li[r])
        li[l],li[r],li[l+1],li[l-1],li[r+1]=0,0,0,0,0
        print(li,"from if")
    elif r<len(li) and max_num>li[l]+li[r] :
        res+=max_num
        li[l],li[r],li[l+1]=0,0,0
        print(li,"from eif")
    elif li.index(max_num)==len(li)-1 and max_num>li[l]:
        res+=max_num
        li[l],li[l+1]=0,0
    k-=1
    all(element == 0 for element in li)
print(li)
print(res)
"""
#or
"""class Solution(object):
    def rob(self, nums):
        
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]

        # Initialize variables
        prev_max = 0  # maximum amount that can be robbed from previous houses
        curr_max = 0  # maximum amount that can be robbed including current house

        # Iterate through the houses
        for num in nums:
            # Calculate the new maximum amount that can be robbed including the current house
            temp = curr_max
            curr_max = max(prev_max + num, curr_max)
            prev_max = temp

        # The final result is the maximum amount that can be robbed
        return curr_max
"""


tuples_list = [(1, 2), (), (3, 4), (5,), (), (6, 7, 8)]
result = []
for t in tuples_list:
    if t:  # Check if the tuple is not empty
        result.append(t)
print( result)
