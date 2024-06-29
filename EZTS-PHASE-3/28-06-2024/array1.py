nums=[1,2,3,4,5,6,7,8,9]
k=3
nums=nums[-k:]+nums[:len(nums)-(k)]
print(nums)