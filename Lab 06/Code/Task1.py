import cv2
"""
Task 1: Bounding Box
"""
def BoundingBox(image, height, width):
	left, right = width, 0
	top, bottom = height, 0

	for x in range(width):
		for y in range(height):
			color = image[y, x]
			if color == 0:
				if x > right:
					right = x
				if x < left:
					left = x
				if y > bottom:
					bottom = y
				if y < top:
					top = y

	return top, bottom, left, right