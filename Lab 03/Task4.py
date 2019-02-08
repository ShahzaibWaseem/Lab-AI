"""
Task 4: Black to White Transitions
"""
def B2W_Transitions(image, width, height, string):
	prevPixel = image[0, 0]
	countB2W = 0

	for x in range(1, width):
		for y in range(1, height):
			currPixel = image[x, y]
			if (currPixel == 255) and (prevPixel == 0):
				countB2W += 1
			prevPixel = currPixel

	print(string + "\t:\t", countB2W)
	return countB2W