import cv2
"""
Task 1: Bounding Box
"""
def BoundingBox(image, height, width):
	left, right = width, 0
	top, bottom = height, 0

	for x in range(0, height):
		for y in range(0, width):
			color = image[x,y]
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