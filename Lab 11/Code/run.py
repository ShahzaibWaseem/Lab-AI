import cv2, math
from utils import *
from glob import glob

rectangles = []

centroids = []
transitions = []
ratios = []
black_Pixels = []
normalized = []
angles = []
normalized_blacks = []

def flushVariables():
	rectangles.clear()
	centroids.clear()
	transitions.clear()
	ratios.clear()
	black_Pixels.clear()
	normalized.clear()
	angles.clear()
	normalized_blacks.clear()

"""
Splitting Image
"""
def SplittingRecursive(image, left, right, top, bottom, depth=0):
	cx, cy, n = FindCentroid(image, left, right, top, bottom)

	if depth < 3:
		SplittingRecursive(image, left, cx, top, cy, depth + 1)			# Top Left
		SplittingRecursive(image, cx, right, top, cy, depth + 1)		# Bottom Left
		SplittingRecursive(image, left, cx, cy, bottom, depth + 1)		# Top Right
		SplittingRecursive(image, cx, right, cy, bottom, depth + 1)		# Bottom Right
	else:
		rectangles.append([(left, top), (right, bottom)])
		transitions.append(B2W_Transitions(image[top:bottom, left:right]))
		ratios.append(AspectRatio(left, right, top, bottom))

		# Task 6
		size = (bottom-top)*(right-left)
		blacks = blackPixels(image, left, right, top, bottom)
		black_Pixels.append(blacks)
		try:
			normalized.append(size/blacks)
		except:
			normalized.append(0)

		cx, cy, n = FindCentroid(image[top:bottom, left:right], 0, right-left, 0, bottom-top)
		centroids.append((cx, cy))

		# Task 7
		angle = math.degrees(math.acos((bottom-top - cy)/(math.sqrt((right-left - cx)**2 + (bottom-top - cy)**2))))
		angles.append(angle)

		normalized_black = blackPixelAngleSummation(image, left, top, right, bottom)
		normalized_blacks.append(normalized_black)

def BulkProcessing(path, directory):
	DATASET_PATH = "../Dataset_4NSigComp2010/"
	TEXT_FILES_PATH = "../Text/"

	for filename in glob(DATASET_PATH + path + directory + "*.png"):
		print("IMAGE FILE: ", filename.split('/')[-1], "\n")
		image = cv2.imread(filename, 0)

		bin_image = Binarization(image)
		height, width = bin_image.shape
		top, bottom, left, right = BoundingBox(bin_image, height, width)

		print("Image Operations")
		SplittingRecursive(bin_image, left, right, top, bottom, 0)

		print("Dumping into Text Files")
		centroidFile = open(TEXT_FILES_PATH + directory + "Centroids/" + filename.split('/')[-1].split('.')[0] + ".txt", "w")
		transitionsFile = open(TEXT_FILES_PATH + directory + "Transitions/" + filename.split('/')[-1].split('.')[0] + ".txt", "w")
		ratiosFile = open(TEXT_FILES_PATH + directory + "Ratios/" + filename.split('/')[-1].split('.')[0] + ".txt", "w")
		blackPixelsFile = open(TEXT_FILES_PATH + directory + "BlackPixels/" + filename.split('/')[-1].split('.')[0] + ".txt", "w")
		normalizedFile = open(TEXT_FILES_PATH + directory + "Normalized/" + filename.split('/')[-1].split('.')[0] + ".txt", "w")
		anglesFile = open(TEXT_FILES_PATH + directory + "Angles/" + filename.split('/')[-1].split('.')[0] + ".txt", "w")
		normalizedBlacksFile = open(TEXT_FILES_PATH + directory + "NormalizedBlacks/" + filename.split('/')[-1].split('.')[0] + ".txt", "w")

		for i in range(len(angles)):
			splitImage = cv2.rectangle(bin_image, (rectangles[i][0][0], rectangles[i][0][1]), (rectangles[i][1][0], rectangles[i][1][1]), (0,0,0), 1)
			centroidFile.write(str(centroids[i][0]) + ", " + str(centroids[i][1]) + "\n")
			transitionsFile.write(str(transitions[i]) + "\n")
			ratiosFile.write(str(ratios[i]) + "\n")
			blackPixelsFile.write(str(black_Pixels[i]) + "\n")
			normalizedFile.write(str(normalized[i]) + "\n")
			anglesFile.write(str(angles[i]) + "\n")
			normalizedBlacksFile.write(str(normalized_blacks[i]) + "\n")

		print("Saving Processed Image")
		cv2.imwrite("../Images/" + directory + filename.split('/')[-1].split('.')[0] + "_out.png", splitImage)

		centroidFile.close()
		transitionsFile.close()
		ratiosFile.close()
		blackPixelsFile.close()
		normalizedFile.close()
		anglesFile.close()
		normalizedBlacksFile.close()

		flushVariables()

path = "TestSet/"
referencePath = "Reference/"
questionedPath = "Questioned/"

# BulkProcessing(path, referencePath)
BulkProcessing(path, questionedPath)