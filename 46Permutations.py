from typing import List
from itertools import permutations
def permute(nums: List[int]) -> List[List[int]]:
  result = permutations(nums)
  result = [item for item in result]
  return result

nums = [1,2,3]

print(permute(nums))