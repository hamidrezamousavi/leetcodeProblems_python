from typing import Optional
from nodes import *

class Solution:
  def most_right_val(self, root:TreeNode)->int:
    pointer= root
    while pointer.right and pointer.right.val != None:
      pointer = pointer.right
    return pointer.val
  
  def most_left_val(self,root:TreeNode)->int:
    pointer= root
    while pointer.left and pointer.left.val != None:
      pointer = pointer.left
    return pointer.val
  
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
    if not root:
      return True
    if root.right == None and root.left == None:
      return True
    
    if self.isValidBST(root.left) and self.isValidBST(root.right) \
       and (root.right == None or self.most_left_val(root.right) > root.val) \
       and(root.left ==None or self.most_right_val(root.left) < root.val):
      return True
    return False