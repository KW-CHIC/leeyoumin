nums = [7, 1, 5, 3, 6, 4]

#풀이1
def stock(nums):
    max_price = 0
    
    '''
    enumerate는 원소와 인덱스 반환하는 함수
    즉, 아래의 for문에서 i는 인덱스, number는 원소
    '''
    for i, number in enumerate(nums):
        for j in range(i, len(nums)):
            max_price = max(nums[j] - number, max_price)
            
    return max_price

print("풀이1의 답")
print(stock(nums))

#풀이2
import sys

def stock2(nums):
    min_nums = sys.maxsize
    res = 0
    
    for numbers in nums:
        min_nums = min(min_nums, numbers)
        res = max(res, numbers - min_nums)
        
    return res

print("풀이2의 답")
print(stock2(nums))