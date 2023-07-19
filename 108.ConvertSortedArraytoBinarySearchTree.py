from nodes import *
from typing import List

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
  if not nums:
    return None
  mid = len(nums)//2
  root = TreeNode(nums[mid])
  root.left = sortedArrayToBST(nums[:mid])
  root.right = sortedArrayToBST(nums[mid+1:])
  return root

nums = [0,1,2,3,4,5]
root = sortedArrayToBST(nums)
print_tree(root)