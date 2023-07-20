from nodes import *
from typing import Optional,Tuple
def get_max(root:Optional[TreeNode])->Tuple[Optional[ int],Optional[ int]]:
  if not root:
    return 0, -2000
  left_max, left_inner = get_max(root.left)  
  right_max, right_inner = get_max(root.right)
  
  outgoing_max = left_max + root.val \
              if left_max > right_max \
              else  right_max + root.val

  outgoing_max = outgoing_max if outgoing_max > root.val else root.val
  
  inner = left_max + right_max + root.val
  inner = max(inner, left_inner, right_inner, outgoing_max)

  return (outgoing_max,inner)
def maxPathSum(root: Optional[TreeNode]) -> int:
  out, inner = get_max(root)
  
  return out if out > inner else inner
root = [2,-1,-2]
root = fill_tree(root)
print(maxPathSum(root))