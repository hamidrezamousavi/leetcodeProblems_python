class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


dia_max = 0


def nodeDia(root):
    global dia_max
    local
    if root.left is None and root.right is None:
        return 0
    if root.left and root.right is None:
        temp = nodeDia(root.left)
        dia_max = temp + 1 if temp + 1 > dia_max else dia_max
        return temp + 1
    if root.right and root.left is None:
        temp = nodeDia(root.right)
        dia_max = temp + 1 if temp + 1 > dia_max else dia_max

        return temp + 1
    r = nodeDia(root.right)
    l = nodeDia(root.left)
    dia_max = r + l + 2 if r + l + 2 > dia_max else dia_max
    if r > l:
        return r+1
    else:
        return l+1


def diameterOfBinaryTree(root):
    nodeDia(root)
    print(dia_max)