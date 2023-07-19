from nodes import *
from typing import List
def return_preorder(root:Optional[TreeNode])-> List[TreeNode]:
  if not root:
    return []
  result = [root]
  if root.left:
    result.extend(return_preorder(root.left))
  if root.right:
    result.extend(return_preorder(root.right))
  return result
  
def flatten(root: Optional[TreeNode]) -> None:
  if not root:
    return 
  flatten_list = return_preorder(root)
  pointer = root
  for node in flatten_list[1:]:
    pointer.right = node
    pointer.left = None
    pointer = pointer.right
  return None

root = [1,2,5,3,4,8,6]
root = fill_tree(root)
print_tree(root)
flatten(root)
print_tree(root)
