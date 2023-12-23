from typing import List, Optional
from nodes import *
from copy import deepcopy
def find_ends(root:TreeNode)->List[TreeNode]:
  if not root.right and not root.left:
    return [root]
  result = []
  if root.left:
    result.extend(find_ends(root.left))
  if root.right:
    result.extend(find_ends(root.right))

  return result


def next_states(root:TreeNode)->List[TreeNode]:
  result = []
  ends = find_ends(root)
  
  for item in ends:
    
    item.left = TreeNode(0)
    item.right = TreeNode(0)
    result.append(deepcopy(root))
    item.left = None
    item.right = None
  
  return result
def allPossibleFBT(n: int) -> List[Optional[TreeNode]]:
  temp = [TreeNode(0)]
  next_state = []
  for i in range(n):
    
    for item in temp:
      
      next_state.extend(next_states(item))
    print(len(next_state))
    temp = next_state
  return next_state

root = [1,2,3,4,5,8,9,None,None,6,7,None,None,10,11]
root = fill_tree(root)
states = allPossibleFBT(3)
for item in states:
  print_tree(item)