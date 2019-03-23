import cv2
import os, shutil			# For Directory Management
import matplotlib.pyplot as plt
import Task0, Task1, Task2, Task3, Task4, Task5

# Deletes the Directory where Text Files are saved
# To avoid updating the txt files while appending text
def CleaningDirectories(path):
	if os.path.exists(path):
		shutil.rmtree(path)

"""
Splitting Image
"""
def SplittingRecursive(image, left, right, top, bottom, depth=0):
	cx, cy = Task2.FindCentroid(image, left, right, top, bottom)
	# print("(", top, "\t", left, ")\t(", bottom, "\t", right, ")\t", cx, "\t", cy, "\tDepth: ", depth)

	if depth < 3:
		SplittingRecursive(image, left, cy, top, cx, depth + 1)		# Top Left
		SplittingRecursive(image, cy, right, top, cx, depth + 1)	# Bottom Left
		SplittingRecursive(image, left, cy, cx, bottom, depth + 1)	# Top Right
		SplittingRecursive(image, cy, right, cx, bottom, depth + 1)	# Bottom Right
	else:
		t = Task4.B2W_Transitions(image, left, right, top, bottom)
		r = Task5.AspectRatio(left, right, top, bottom)

		filePath = "../Text/"
		# If Path Does not exists; Create it
		if not os.path.exists(filePath):
			os.makedirs(filePath + "Transitions/")
			os.makedirs(filePath + "Ratios/")
			os.makedirs(filePath + "Centroids/")

		TransitionsFile = open(filePath + "Transitions/" + "signature.txt", "a")
		TransitionsFile.write(str(t) + "\n")
		TransitionsFile.close()

		RatiosFile = open(filePath + "Ratios/" + "signature.txt", "a")
		RatiosFile.write(str(r) + "\n")
		RatiosFile.close()

		CentroidsFile = open(filePath + "Centroids/" + "signature.txt", "a")
		CentroidsFile.write(str(cx) + "," + str(cy) + "\n")
		CentroidsFile.close()

	return cv2.rectangle(bin_image, (top, left), (bottom, right), (0,255,0), 1)

path = "../Images/"
filename = "signature.jpg"

# Opening Image
if len(filename.split('.')) == 2:
	image = cv2.imread(path + filename, 0)

# Task 0
filename = path + "bin_" + filename
bin_image = Task0.Binarization(image, filename)

filename = filename.split('/')[-1]
# Task 1
height, width = bin_image.shape
filename = path + "box_" + filename
top, bottom, left, right = Task1.BoundingBox(bin_image, height, width)
bounding_box_image = cv2.rectangle(bin_image, (top, left), (bottom, right), (0,255,0), 3)

cv2.imwrite(filename, bounding_box_image)
B = (left, right, top, bottom)

filename = filename.split('/')[-1]
# Task 2
filename = path + "cen_" + filename
cx, cy = Task2.FindCentroid(bin_image, 0, bin_image.shape[1], 0, bin_image.shape[0])
centroid_image = cv2.circle(bounding_box_image, (cy, cx), 10, 200, -1)

cv2.imwrite(filename, centroid_image)
C = (cx, cy)

filename = filename.split('/')[-1]
# Task 3
filename = path + "seg_" + filename
top_left, bottom_left, top_right, bottom_right, segmented_image = Task3.DivideBoundingBox(centroid_image, top, bottom, left, right, cx, cy)

cv2.imwrite(filename, segmented_image)
filename = filename.split('/')[-1]
CleaningDirectories("../Text/")
image = SplittingRecursive(bin_image, left, right, top, bottom, 0)
cv2.imshow("image", image)
filename = filename.split('/')[-1]
filename = path + "final_" + filename
cv2.imwrite(filename, image)

cv2.waitKey(0)