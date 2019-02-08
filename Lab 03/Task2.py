import cv2
"""
Task 2: Finding Centroid
"""
def FindCentroid(width, height, image, bounding_box_image, filename):
	cx, cy = 0, 0
	n = 0
	for x in range(0, width):
		for y in range(0, height):
			if image[x, y] == 0:
				cx = cx + x
				cy = cy + y
				n = n + 1

	cx = cx / n
	cy = cy / n

	print("\nCentroid")
	print("cx\t:\t", cx, "\tcy\t:\t", cy)

	centroid_image = cv2.circle(bounding_box_image, (int(cy), int(cx)), 10, 200, -1)
	cv2.imwrite(filename, centroid_image)

	return centroid_image, cx, cy