import cv2
"""
Task 2: Finding Centroid
"""
def FindCentroid(image, left, right, top, bottom):
	cx, cy = 0, 0
	n = 1

	for x in range(top, bottom):
		for y in range(left, right):
			if image[x, y] == 0:
				cx = cx + x
				cy = cy + y
				n = n + 1

	cx = cx // n
	cy = cy // n

	return cx, cy