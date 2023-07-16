from typing import List
from bisect import bisect_left
def search(nums: List[int], target: int) -> int:
  pivot_num = min(nums)
  pivot_index = nums.index(pivot_num)  
  if pivot_index == 0:
    pivot_index = len(nums) - 1
  result = -1
  if target >= nums[0]:
    expect_index = bisect_left(nums,target,0, pivot_index)
    if nums[expect_index] == target:
      result = expect_index
  else:
    print('<')
    expect_index = bisect_left(nums,target, pivot_index, len(nums))
    if len(nums)> expect_index and nums[expect_index] == target:
      result = expect_index

  return result

nums = [1,3]
target = 3
print(search(nums, target))