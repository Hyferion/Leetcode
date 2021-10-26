class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printNode(self, node):
        if node:
            printNode(node.left)

            printNode(node.right)

            print(node.val)

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.printNode(root)
