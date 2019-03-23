import cv2
"""
Preprocessing - Image Binarization
"""
def Binarization(image, filename):
	retval, binarized_img = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
	cv2.imwrite(filename, binarized_img)

	return binarized_img