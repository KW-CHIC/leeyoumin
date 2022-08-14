#책에 있는 스택 쌓기 방법으로 코드 작성하며 공부함

#입력값
nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

#함수 시작
def trapping(nums):
    stack = []
    volume = 0
    
    for i in range(len(nums)):  #입력한 리스트의 원소 개수만큼 반복
        while stack and nums[i] > nums[stack[-1]]:  #변곡점을 만나면
            top = stack.pop()   #stack 리스트의 마지막 함수 꺼냄
            
            if not len(stack):  #stack 리스트 원소가 없을 경우 아래 코드 실행 안함
                break
            
            distance = i - stack[-1] - 1    
            waters = min(nums[i], nums[stack[-1]]) - nums[top]
            
            volume += distance * waters
        
        stack.append(i)
    return volume

print(trapping(nums))