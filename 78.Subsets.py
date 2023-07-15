from typing import List
from itertools import combinations
def subsets(nums: List[int]) -> List[List[int]]:
  result = []
  for i in range(len(nums)+1):
    result.extend(combinations(nums, i))
  result = [list(item) for item in result]
  for item in result:
    print(item)
  return result

nums = [1,2,3]
print(subsets(nums))