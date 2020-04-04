def selectionSort(array):
    # holds current index
	currentIdx = 0

    # while loops will repeat until it is greater than array length
	while currentIdx < len(array) -1:
        # this variable will be used to check the current index and the next one
		smallestIdx = currentIdx
		# starts for loop next to current index 
		for i in range(currentIdx + 1, len(array)):
			# checks index if it is greater or less than
			if array[smallestIdx] > array[i]:
				# updates smallest index with the current index if it is less than the next index 
				smallestIdx = i
		# we swapp places of the index
		array[currentIdx], array[smallestIdx] = array[smallestIdx], array[currentIdx]

		# current index is now incremented to test next number
		currentIdx += 1
	# once the array is sorted return
	return array