"""
Task 6: Normalization
"""
def Normalization(image, left, right, top, bottom, transitions):
	width = right - left
	height = bottom - top

	return (width * height) / transitions