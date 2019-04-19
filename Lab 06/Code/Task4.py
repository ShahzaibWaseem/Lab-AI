"""
Task 4: Black to White Transitions
"""
def B2W_Transitions(image):
	height, width = image.shape
	countB2W = 0
	prevPixel = image[0, 0]

	for x in range(width):
		for y in range(height):
			currPixel = image[y, x]

			if (currPixel == 255) and (prevPixel == 0):
				countB2W += 1
			prevPixel = currPixel

	return countB2W