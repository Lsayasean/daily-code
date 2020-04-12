def threeNumberSum(array, targetSum):
    # we want to sort the array so we can set up the pointers of left and right
	array.sort()
	triplets = []
	
	# we use -2 because we are taking position 1, i+1 and range of i
	for i in range(len(array) -2):
		# setting up pointers
		left = i + 1
		right = len(array) - 1
		while left < right:
			# total of sum
			currentSum = array[i] + array[left] + array[right]
			if currentSum == targetSum:
				triplets.append([array[i], array[left], array[right]])
				# moves both pointers to reset the sum
				left += 1
				right -=1
			elif currentSum < targetSum:
				# move left pointer up one if our current is less than target
				left += 1
			elif currentSum > targetSum:
				# moved right pointer 1 over to decrease the target sum
				right -= 1
	return triplets