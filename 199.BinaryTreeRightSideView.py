from nodes import *
from typing import Optional,List
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
    result.append(temp[-1])
  return result