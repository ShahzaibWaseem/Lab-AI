import cv2, math

"""
Preprocessing - Image Binarization
"""
def Binarization(image):
	retval, binarized_img = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
	return binarized_img

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

"""
Task 4: Black to White Transitions
"""
def B2W_Transitions(image):
	height, width = image.shape
	countB2W = 0

	if height == 0 or width == 0:
		return 0
	prevPixel = image[0, 0]

	for x in range(width):
		for y in range(height):
			currPixel = image[y, x]

			if (currPixel == 255) and (prevPixel == 0):
				countB2W += 1
			prevPixel = currPixel

	return countB2W

"""
Task 5: Finding Aspect Ratio
"""
def AspectRatio(left, right, top, bottom):
	if (bottom - top) == 0:
		return 0
	return (right - left)/(bottom - top)

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

"""
Task: Black Pixel - Angle Summation
"""
def blackPixelAngleSummation(image, left, top, right, bottom):
	sum = 0
	blackCount = 0
	for x in range(left, right):
		for y in range(top, bottom):
			pixel = image[y,x]
			if pixel == 0:
				blackCount += 1
				if(x == left):
					sum += math.pi / 2
				else:
					sum += math.atan((float) (bottom-y)  / (float) (x-left))
	if blackCount == 0:
		return 0
	return sum / blackCount
