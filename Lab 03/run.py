import cv2
import matplotlib.pyplot as plt
import Task0, Task1, Task2, Task3, Task4

filename = "signature.jpg"

# Opening Image
if len(filename.split('.')) == 2:
	image = cv2.imread(filename, 0)

# Task 0
filename = "bin_" + filename
bin_image = Task0.Binarization(image, filename)
# cv2.imshow("Binarization", bin_image)

# Task 1
width, height = bin_image.shape
filename = "box_" + filename
top, bottom, left, right, bounding_box_image = Task1.BoundingBox(width, height, bin_image, filename)
B = (left, right, top, bottom)
# cv2.imshow("Bounding Box", bounding_box_image)

# Task 2
filename = "cen_" + filename
centroid_image, cx, cy = Task2.FindCentroid(width, height, bin_image, bounding_box_image, filename)
C = (cx, cy)
# cv2.imshow("Centroid", centroid_image)

# Task 3
cx = int(cx)
cy = int(cy)
filename = "seg_" + filename
top_left, bottom_left, top_right, bottom_right, segmented_image = Task3.DivideBoundingBox(centroid_image, top, bottom, left, right, cx, cy, filename)

cv2.imshow("Top Left", top_left)
cv2.imshow("Bottom Left", bottom_left)
cv2.imshow("Top Right", top_right)
cv2.imshow("Bottom Right", bottom_right)

print("\nNumber of Black to White Transitions")

# Task 4
TL = Task4.B2W_Transitions(top_left, top_left.shape[0], top_left.shape[1], "Top Left")
BL = Task4.B2W_Transitions(bottom_left, bottom_left.shape[0], bottom_left.shape[1], "Bottom Left")
TR = Task4.B2W_Transitions(top_right, top_right.shape[0], top_right.shape[1], "Top Right")
BR = Task4.B2W_Transitions(bottom_right, bottom_right.shape[0], bottom_right.shape[1], "Bottom Right")
T = (TL, TR, BL, BR)

cv2.waitKey(0)