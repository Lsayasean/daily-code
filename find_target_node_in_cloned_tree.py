# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# implementing this with DFS
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        reference = None
        def traverseTree(original, cloned, target):
            # something new I learned, nonlocal keywork to bring in a non local variable
            nonlocal reference
            if cloned is not None:
                if cloned.val == target.val:
                    reference = cloned
                    return
                else:
                    # implementing DFS on BOTH tree to traverse from left to right
                    traverseTree(cloned.left, target)
                    traverseTree( cloned.right, target)
            else:
                return
        traverseTree(cloned, target)
        return reference

# anothery way to implement this with BFS
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = [cloned]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.val == target.val:
                return current
            else:
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)