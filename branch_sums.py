# write a function that takes in a Binary tree and returns a list of its branch sums
# to rightmost branch sum, a brnach sum is the sum of all values in a Binary Tree Branch
# A Binray tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node
# each Binary tree has a int value, a left and a right child node.  Children nodes can either be
# Nomaru tree nodes themselves or None / null

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
	calcBranchSums(root, 0, sums)
	return sums

def calcBranchSums(node , runningSum , sums):
	if node is None:
		return
	
	newRunningSum = runningSum + node.value
	if node.left is None and node.right is None:
		sums.append(newRunningSum)
		return
	
	calcBranchSums(node.left, newRunningSum, sums)
	calcBranchSums(node.right, newRunningSum, sums)