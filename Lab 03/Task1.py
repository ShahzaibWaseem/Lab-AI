import cv2
"""
Task 1: Bounding Box
"""
def BoundingBox(width, height, image, filename):
	left, right = width, 0
	top, bottom = height, 0

	for x in range(0, width):
		for y in range(0, height):
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
	print("Bounding Box")
	print("Top\t:\t", top, "\t\t\tBottom\t:\t", bottom)
	print("Left\t:\t", left, "\t\t\tRight\t:\t", right)

	bounding_box_image = cv2.rectangle(image, (top, left), (bottom, right), (0,255,0), 3)
	cv2.imwrite(filename, bounding_box_image)

	return top, bottom, left, right, bounding_box_image