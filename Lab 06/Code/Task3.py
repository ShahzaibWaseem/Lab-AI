import cv2
"""
Task 3: Dividing Centroid
"""
def DivideBoundingBox(centroid_image, top, bottom, left, right, cx, cy):
	segmented_image = cv2.rectangle(centroid_image, (left, top), (cx, cy), (0,255,0), 3)		# top left
	segmented_image = cv2.rectangle(segmented_image, (cx, top), (right, cy), (0,255,0), 3)		# bottom left
	segmented_image = cv2.rectangle(segmented_image, (left, cy), (cx, bottom), (0,255,0), 3)	# top right
	segmented_image = cv2.rectangle(segmented_image, (cx, cy), (right, bottom), (0,255,0), 3)	# bottom right

	top_left = centroid_image[left: cx, top: cy]
	bottom_left = centroid_image[cx: right, top: cy]
	top_right = centroid_image[left: cx, cy: bottom]
	bottom_right = centroid_image[cx: right, cy: bottom]

	return top_left, bottom_left, top_right, bottom_right, segmented_image