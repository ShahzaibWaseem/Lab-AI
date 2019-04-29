import numpy as np
import pandas as pd
import re
from glob import glob

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

# Variables for Questioned Images
q_centroids = {}
q_transitions = {}
q_ratios = {}
q_black_Pixels = {}
q_normalized = {}
q_angles = {}
q_normalized_blacks = {}
x = []
y = []
titles = ['Centroids', 'Transitions', 'Ratios', 'BlackPixels', 'Normalized', 'Angles', 'NormalizedBlacks']

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

def main():
	loadVariables("Questioned")
	key = pd.read_csv("../Text/key.csv")

	for questioned_iterator in q_transitions.keys():
		data = []
		data.append(np.mean(np.array(q_centroids[questioned_iterator])))
		data.append(np.mean(np.array(q_transitions[questioned_iterator])))
		data.append(np.mean(np.array(q_ratios[questioned_iterator])))
		data.append(np.mean(np.array(q_black_Pixels[questioned_iterator])))
		data.append(np.mean(np.array(q_normalized[questioned_iterator])))
		data.append(np.mean(np.array(q_angles[questioned_iterator])))
		data.append(np.mean(np.array(q_normalized_blacks[questioned_iterator])))
		x.append(data)

	for temp, file in enumerate(q_ratios.keys()):
		number = str(re.findall(r'\d+', file)).replace('[', '').replace(']', '').replace("'", '').lstrip('0')
		if key['Decision'].values[int(number) - 1] == 'F':
			y.append(0)
		if key['Decision'].values[int(number) - 1] == 'D':
			y.append(1)
		if key['Decision'].values[int(number) - 1] == 'G':
			y.append(2)

	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

	print('K Nearest Neighbors')
	for k in range(1, 6):
		knnClassifier = KNeighborsClassifier(n_neighbors=k, n_jobs=-1)
		knnClassifier.fit(x_train, y_train)
		print('kNN accuracy with k =', k, '\t:\t', knnClassifier.score(x_test, y_test))

	print('\nNaive Bayes')
	nbClassifier = GaussianNB()
	nbClassifier.fit(x_train, y_train)
	print('Naive Bayes accuracy\t\t:\t', nbClassifier.score(x_test, y_test))

	print('\nDecision Trees...')
	dtClassifier = DecisionTreeClassifier(random_state=21)
	dtClassifier.fit(x_train, y_train)
	print('Decision Tree accuracy\t\t:\t', dtClassifier.score(x_test, y_test))

if __name__ == '__main__':
	main()