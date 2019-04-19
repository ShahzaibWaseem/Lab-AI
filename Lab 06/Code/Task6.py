"""
Task 6: Black Pixels
"""
def blackPixels(image, left, right, top, bottom):
	blackCount = 0

	for x in range(left, right):
		for y in range(top, bottom):
			currentPixel = image[y, x]
			if (currentPixel == 0):
				blackCount += 1

	return blackCount