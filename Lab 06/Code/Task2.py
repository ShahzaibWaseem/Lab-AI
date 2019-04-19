import cv2
"""
Task 2: Finding Centroid
"""
def FindCentroid(image, left, right, top, bottom):
	cx, cy = 0, 0
	n = 0

	for x in range(left, right):
		for y in range(top, bottom):
			if image[y, x] == 0:
				cx = cx + x
				cy = cy + y
				n = n + 1
	if n == 0:
		return ((left + right) // 2, (top + bottom) // 2, n)
	else:
		return (cx // n, cy // n, n)