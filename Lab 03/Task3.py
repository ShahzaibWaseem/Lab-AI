import cv2
"""
Task 3: Dividing Centroid
"""
def DivideBoundingBox(centroid_image, top, bottom, left, right, cx, cy, filename):
	segmented_image = cv2.rectangle(centroid_image, (top, left), (cy, cx), (0,255,0), 3)		# top left
	segmented_image = cv2.rectangle(segmented_image, (top, cx), (cy, right), (0,255,0), 3)		# bottom left
	segmented_image = cv2.rectangle(segmented_image, (cy, left), (bottom, cx), (0,255,0), 3)	# top right
	segmented_image = cv2.rectangle(segmented_image, (cy, cx), (bottom, right), (0,255,0), 3)	# bottom right

	top_left = centroid_image[left: cx, top: cy]
	bottom_left = centroid_image[cx: right, top: cy]
	top_right = centroid_image[left: cx, cy: bottom]
	bottom_right = centroid_image[cx: right, cy: bottom]

	cv2.imwrite(filename, segmented_image)
	return top_left, bottom_left, top_right, bottom_right, segmented_image