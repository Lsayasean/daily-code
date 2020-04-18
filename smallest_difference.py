def smallestDifference(arrayOne, arrayTwo):
	# make copies and sort the copied array
	newArrOne = arrayOne[:]
	newArrTwo = arrayTwo[:]
    # if we do not want to make copies we just sort in place, ex. arrayOne.sort()
	newArrOne.sort()
	newArrTwo.sort()
	# set smallest number and current to infinity at the start
	smallestNum = float("inf")
	currentNum = float("inf")
	smallestPair = []
	
	# needed to set and move pointers 
	indexOne = 0
	indexTwo = 0
	
	while indexOne < len(newArrOne) and indexTwo < len(newArrTwo):
		# sets the pointers to each array
		firstNum = newArrOne[indexOne]
		secondNum = newArrTwo[indexTwo]
		if firstNum < secondNum:
			# set current number
			currentNum = secondNum - firstNum
			# move pointer based on which is smaller than the other
			indexOne += 1
		elif secondNum < firstNum:
			currentNum = firstNum - secondNum
			indexTwo += 1
		else:
			# return if the numbers are the same cause it will = 0
			return [firstNum, secondNum]
		if smallestNum > currentNum:
			smallestNum = currentNum
			smallestPair = [firstNum, secondNum]
	return smallestPair