# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:
# Search for a node to remove.
# If the node is found, delete the node.
# Example 1:
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            

            successor = self.findMin(root.right)
            root.val = successor.val

            root.right = self.deleteNode(root.right, successor.val)
        
        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
