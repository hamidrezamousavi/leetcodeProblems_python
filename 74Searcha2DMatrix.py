from typing import List
from bisect import bisect_left
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
  flattened = [x for item in matrix for x in item]
  expected_index = bisect_left(flattened, target)
  if expected_index < len(flattened) and \
     flattened[expected_index ] == target:
    return True
  
  return False

matrix = [[1]]
target = 1
print(searchMatrix(matrix, target))