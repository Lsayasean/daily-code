def findClosestValueInBst(tree, target):
    # a helper is used to help keep to start the closest value
    start = tree.value
	return helper(tree, target, start)

def helper(tree, target, closest):
    # finish the recursion when tree.value is none
	if tree is None:
		return closest
    # checkes to see which value is closer to target
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
    if target > tree.value:
		return helper(tree.right, target, closest)
	elif target < tree.value:
		return helper(tree.left, target, closest)
	else:
        # if closest value == target
		return closest