nums = [1, 4, 3, 2]

def Sums(nums):
    nums.sort()
    res = 0
    res2 = []
    
    for i in nums:
        res2.append(i)
        if len(res2) == 2:
            res += min(res2)
            res2 = []
    return res

print(Sums(nums))