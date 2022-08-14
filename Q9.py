nums = [-1, 0, 1, 2, -1, -4]

def threeSums(nums):
    res = []
    nums.sort()
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i] +nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
    return res

print(threeSums(nums))   
#위의 코드로 실행할 경우 중복도 출력됨
     
#책 코드
def threeSum(nums):
    result = []
    nums.sort()
    for i in range(0, len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-1):
            if j>i+1 and nums[j] == nums[j-1]:
                continue
            for k in range(j+1, len(nums)):
                if k>j+1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] +nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
    return result
                 
print(threeSum(nums))