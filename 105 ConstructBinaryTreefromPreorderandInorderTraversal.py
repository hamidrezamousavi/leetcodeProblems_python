from typing import List
from nodes import *
def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
  if not preorder:
    return None
  if len(preorder) == 1:
    return TreeNode(preorder[0])

  root = TreeNode(preorder[0])
  root_val_index = inorder.index(root.val)
  
  left_inorder = inorder[:root_val_index]
  print('left_inorder', left_inorder)
  left_preorder = preorder[1:len(left_inorder)+1]
  print('left_preorder', left_preorder)
  root.left = buildTree(left_preorder, left_inorder)
  
  right_inorder = inorder[root_val_index + 1:]
  print('right_inorder', right_inorder)
  right_preorder = preorder[1+len(left_inorder):]
  print('right_preorder', right_preorder)
  root.right = buildTree(right_preorder, right_inorder)
  print('-----------')
  return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root  = buildTree(preorder, inorder)
print_tree(root)