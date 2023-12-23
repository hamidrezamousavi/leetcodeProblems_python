from nodes import *
from typing import Tuple, List
def find_parents(root:'TreeNode', p:'TreeNode')-> Tuple['bool', List['TreeNode']]:
  print(root.val)
  

  if not root:
    
    print('b')
    return False ,None
  if root.val == p.val:
    print('b')
    return True, []
  if root.left:
    print(root.left.val, 'left')
    check, parent = find_parents(root.left, p)
    if check:
      
      return True, parent.append(root)
  if root.right:
    check, parent = find_parents(root.right, p)
    if check:
      return True, parent.append(root)
  return []
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
  check, parents = find_parents(root, p)
  print(parents)
  for item in parents:
    print(item.val)
  return TreeNode(0)

root = [1,2,3]
root = fill_tree(root)
p = 3
q = 1
lowestCommonAncestor(root, TreeNode(p), TreeNode(q))