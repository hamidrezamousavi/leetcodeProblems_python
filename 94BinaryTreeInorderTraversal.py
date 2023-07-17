from nodes import *
from typing import Optional, List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
  pointer = root
  stack = [root]
  nodes_parent = {root:None}
  result = []
  while stack and stack[0] != None:
    if pointer.left:
      stack.append(pointer.left)
      temp = pointer.left 
      pointer.left = None
     # nodes_parent[pointer.left] = pointer
      pointer = temp
    else:
      if pointer.val != None:
        result.append(pointer.val)
      stack.pop()
      if pointer.right:
        stack.append(pointer.right)
        temp = pointer.right 
        pointer.right= None
        #nodes_parent[pointer.right] = pointer
        pointer = temp
      else:
        if stack:
          pointer = stack[-1]
   # for item in stack:
   #   print(item.val, end = '')
   # print() 
        
  
  return result
root = [1,2,4,2,2,3]
root = fill_tree(root)
print_tree(root)
print(inorderTraversal(root))