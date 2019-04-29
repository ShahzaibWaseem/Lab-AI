import cv2
from glob import glob
import numpy as np

# Variables for Questioned Images
q_centroids = {}
q_transitions = {}
q_ratios = {}
q_black_Pixels = {}
q_normalized = {}
q_angles = {}
q_normalized_blacks = {}

# Variables for Reference Images
r_centroids = {}
r_transitions = {}
r_ratios = {}
r_black_Pixels = {}
r_normalized = {}
r_angles = {}
r_normalized_blacks = {}

"""
Loads Variable
directoryType should be "Questioned" or "Reference" to read the corresponding .txt Files
"""
def loadVariables(directoryType):
	for directory in glob("../Text/" + directoryType + "/*"):
		for textFilePath in glob(directory + "/*"):
			path = textFilePath.split('/')
			textFileName = textFilePath.split('/')[-1].split('.')[0]
			with open(textFilePath, "r+") as textFile:
				data = textFile.readlines()
				data = [line.replace('\n', '') for line in data]
				if path[3] == "Angles":
					data = [float(x) for x in data]
					if directoryType == "Reference": r_angles[textFileName] = data
					if directoryType == "Questioned": q_angles[textFileName] = data
				if path[3] == "BlackPixels":
					data = [int(x) for x in data]
					if directoryType == "Reference": r_black_Pixels[textFileName] = data
					if directoryType == "Questioned": q_black_Pixels[textFileName] = data
				if path[3] == "Centroids":
					centroids_list = []
					for x in data:
						cx, cy = x.split(',')
						centroidPoint = (int(cx), int(cy))
						centroids_list.append(centroidPoint)
					if directoryType == "Reference": r_centroids[textFileName] = centroids_list
					if directoryType == "Questioned": q_centroids[textFileName] = centroids_list
				if path[3] == "Normalized":
					data = [float(x) for x in data]
					if directoryType == "Reference": r_normalized[textFileName] = data
					if directoryType == "Questioned": q_normalized[textFileName] = data
				if path[3] == "NormalizedBlacks":
					data = [float(x) for x in data]
					if directoryType == "Reference": r_normalized_blacks[textFileName] = data
					if directoryType == "Questioned": q_normalized_blacks[textFileName] = data
				if path[3] == "Ratios":
					data = [float(x) for x in data]
					if directoryType == "Reference": r_ratios[textFileName] = data
					if directoryType == "Questioned": q_ratios[textFileName] = data
				if path[3] == "Transitions":
					data = [int(x) for x in data]
					if directoryType == "Reference": r_transitions[textFileName] = data
					if directoryType == "Questioned": q_transitions[textFileName] = data

def euclideanDistance(reference, questioned):
	return sum([(a - b) ** 2 for a, b in zip(reference, questioned)])

def main():
	loadVariables("Reference")
	loadVariables("Questioned")
	distancesFile = open("../Text/distances.csv", "w")
	distancesFile.write("ReferenceSignature,QuestionedSignature,Centroids,Transitions,Ratios,BlackPixels,Normalized,Angles,NormalizedBlacks\n")
	for reference_iterator in r_transitions.keys():
		for questioned_iterator in q_transitions.keys():
			centroidDistance = str( (euclideanDistance(r_centroids[reference_iterator][0], q_centroids[questioned_iterator][0]) + euclideanDistance(r_centroids[reference_iterator][1], q_centroids[questioned_iterator][1])) ** .5)
			transitionDistance = str(euclideanDistance(r_transitions[reference_iterator], q_transitions[questioned_iterator]) ** .5)
			ratioDistance = str(euclideanDistance(r_ratios[reference_iterator], q_ratios[questioned_iterator]) ** .5)
			blackPixelsDistance = str(euclideanDistance(r_black_Pixels[reference_iterator], q_black_Pixels[questioned_iterator]) ** .5)
			normalizedDistance = str(euclideanDistance(r_normalized[reference_iterator], q_normalized[questioned_iterator]) ** .5)
			anglesDistance = str(euclideanDistance(r_angles[reference_iterator], q_angles[questioned_iterator]) ** .5)
			normalizedBlacksDistance = str(euclideanDistance(r_normalized_blacks[reference_iterator], q_normalized_blacks[questioned_iterator]) ** .5)
			string = reference_iterator + "," + questioned_iterator + "," + centroidDistance + "," + transitionDistance + "," + ratioDistance + "," + blackPixelsDistance + "," + normalizedDistance + "," + anglesDistance + "," + normalizedBlacksDistance + "\n"
			distancesFile.write(string)
	distancesFile.close()

if __name__ == '__main__':
	main()