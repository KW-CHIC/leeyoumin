nums = [1,2,3,4]

def Multi(nums):
    res = 1
    result = []
    
    for num in range(0, len(nums)):
        for i in range(0, len(nums)):
            if i != num:
                res = res * nums[i]
        result.append(res)
        res = 1
    return result

print(Multi(nums))    