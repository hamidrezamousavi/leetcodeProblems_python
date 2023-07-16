from typing import List
def findMin(nums: List[int]) -> int:
  if nums[0] <= nums[-1]:
    return nums[0]
  left = 0
  right = len(nums) -1
  pointer = (right + left) // 2
  while left != pointer and right != pointer:
   # print("b",'l', left,'p',pointer,'r', right,)
    if nums[pointer] < nums[right]:
      right = pointer
      pointer = (right + left) // 2
    else:
      left = pointer
      pointer = (right + left)// 2
     
   # print('l', left,'p',pointer,'r', right,)
  return nums[pointer +1] 
  

nums = [4,5,6,7,0,1,2]
print(findMin(nums))