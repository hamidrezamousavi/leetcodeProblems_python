def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
  if not root:
    return root
  if not root.right and not root.left:
    return root
  temp1 = self.invertTree(root.left)
  temp2 = self.invertTree(root.right)
  root.right = temp1
  root.left = temp2
  return root