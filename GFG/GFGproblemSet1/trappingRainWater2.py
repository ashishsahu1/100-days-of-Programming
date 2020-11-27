def findWater(arr, n):

	# left[i] contains height of tallest bar to the
	# left of i'th bar including itself
	left = [0]*n

	# Right [i] contains height of tallest bar to
	# the right of ith bar including itself
	right = [0]*n

	# Initialize result
	water = 0

	# Fill left array
	left[0] = arr[0]
	for i in range( 1, n):
		left[i] = max(left[i-1], arr[i])

	# Fill right array
	right[n-1] = arr[n-1]
	for i in range(n-2, -1, -1):
		right[i] = max(right[i + 1], arr[i]);


	for i in range(0, n):
		water += min(left[i], right[i]) - arr[i]

	return water



arr = [3,0,2,0,4]
n = len(arr)
print("Maximum water that can be accumulated is", findWater(arr, n))

