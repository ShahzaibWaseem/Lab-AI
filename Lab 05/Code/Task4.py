"""
Task 4: Black to White Transitions
"""
def B2W_Transitions(image, left, right, top, bottom):
	prevPixel = image[left, top]
	countB2W = 0

	for x in range(top, bottom):
		for y in range(left, right):
			currPixel = image[x, y]
			if (currPixel == 255) and (prevPixel == 0):
				countB2W += 1
			prevPixel = currPixel

	return countB2W