nums = [2, 7, 11, 15]
target = 9

def TwoSum(nums, target):
    length = len(nums)
    for i in range(0, length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                return [i, j]  
    
res = TwoSum(nums, target)
print(res)