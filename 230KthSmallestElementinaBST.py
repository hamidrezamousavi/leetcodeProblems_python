from nodes import *
from typing import Optional
def get_list(root:Optional[TreeNode])->List[TreeNode]:
  if not root:
    return []
  result = []
  if root.left:
    result =  get_list(root.left)
  result.append(root)
  if root.right:
    result = result + get_list(root.right)
  return result

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
  list_of_nodes = get_list(root)
  return list_of_nodes[k - 1].val

root = [5,3,7,1,4,6,9]
root = fill_tree(root)
k = 6
print(kthSmallest(root, k))