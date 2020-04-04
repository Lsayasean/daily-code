def insertionSort(array):
# loops through the list/array 
	for i in range(1, len(array)):
		# as it loops through it checks the value, if its higher it moves it 
		while i > 0 and array[i] < array[i - 1]:
			array[i], array[i - 1] = array[i - 1], array[i]
			i -= 1
	return array