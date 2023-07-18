from nodes import *
from typing import Optional, List
def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
  if not root:
      return []
  result = []
  parent = [root]
  child = [None]
  while child:
    child = []
    temp = [] 
    for item in parent:
      if item:
        temp.append(item.val)
        if item.left:
          child.append(item.left)
        if item.right:
          child.append(item.right)
    parent = child
    result.append(temp)
  return result
      
      
  
root = [3,9,20,None,None,15,7]
root = fill_tree(root)
print_tree(root)
print(levelOrder(root))