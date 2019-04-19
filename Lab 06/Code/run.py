import cv2, math
import Task0, Task1, Task2, Task4, Task5, Task6

rectangles = []

transitions = []
ratios = []
centroids = []
normalized = []		# Feature 1
angles = []			# Feature 2

"""
Splitting Image
"""
def SplittingRecursive(image, left, right, top, bottom, depth=0):
	cx, cy, n = Task2.FindCentroid(image, left, right, top, bottom)

	if depth < 3:
		SplittingRecursive(image, left, cx, top, cy, depth + 1)			# Top Left
		SplittingRecursive(image, cx, right, top, cy, depth + 1)		# Bottom Left
		SplittingRecursive(image, left, cx, cy, bottom, depth + 1)		# Top Right
		SplittingRecursive(image, cx, right, cy, bottom, depth + 1)		# Bottom Right
	else:
		rectangles.append([(left, top), (right, bottom)])
		transitions.append(Task4.B2W_Transitions(image[top:bottom, left:right]))
		ratios.append(Task5.AspectRatio(left, right, top, bottom))

		# Task 6
		size = (bottom-top)*(right-left)
		blacks = Task6.blackPixels(image, left, right, top, bottom)

		try:
			normalized.append(size/blacks)
		except:
			normalized.append(0)

		cx, cy, n = Task2.FindCentroid(image[top:bottom, left:right], 0, right-left, 0, bottom-top)
		centroids.append((cx, cy))

		# Task 7
		angle = math.degrees(math.acos((bottom-top - cy)/(math.sqrt((right-left - cx)**2 + (bottom-top - cy)**2))))
		angles.append(angle)

path = "../Images/"
filename = "signature.jpg"
TEXT_FILES_PATH = "../Text/"
# Opening Image
if len(filename.split('.')) == 2:
	image = cv2.imread(path + filename, 0)

bin_image = Task0.Binarization(image, filename)

height, width = bin_image.shape
top, bottom, left, right = Task1.BoundingBox(bin_image, height, width)

SplittingRecursive(bin_image, left, right, top, bottom, 0)

centroidFile = open(TEXT_FILES_PATH + "Centroids/" + filename.split('.')[0] + ".txt", "w")
transitionsFile = open(TEXT_FILES_PATH + "Transitions/" + filename.split('.')[0] + ".txt", "w")
ratiosFile = open(TEXT_FILES_PATH + "Ratios/" + filename.split('.')[0] + ".txt", "w")
feature1File = open(TEXT_FILES_PATH + "Feature1/" + filename.split('.')[0] + ".txt", "w")
feature2File = open(TEXT_FILES_PATH + "Feature2/" + filename.split('.')[0] + ".txt", "w")

for i in range(len(angles)):
	splitImage = cv2.rectangle(bin_image, (rectangles[i][0][0], rectangles[i][0][1]), (rectangles[i][1][0], rectangles[i][1][1]), (0,0,0), 1)
	centroidFile.write(str(centroids[i][0]) + ", " + str(centroids[i][1]) + "\n")
	transitionsFile.write(str(transitions[i]) + "\n")
	ratiosFile.write(str(ratios[i]) + "\n")
	feature1File.write(str(normalized[i]) + "\n")
	feature2File.write(str(angles[i]) + "\n")

cv2.imwrite(path + filename.split('.')[0] + "_out.jpg", splitImage)
centroidFile.close()
transitionsFile.close()
ratiosFile.close()
feature1File.close()
feature2File.close()