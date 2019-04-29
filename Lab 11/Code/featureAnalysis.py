import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

disguised = ['Q006', 'Q015', 'Q028', 'Q029', 'Q034', 'Q087', 'Q090']
genuine = ['Q049', 'Q052', 'Q066']
titles = ['Centroids', 'Transitions', 'Ratios', 'BlackPixels', 'Normalized', 'Angles', 'NormalizedBlacks']

def main():
	distancesFile = pd.read_csv("../Text/distances.csv")
	distancesFile = distancesFile.sample(frac=1)	# Random

	plt.rcParams["figure.figsize"] = [22, 15]		# Enlarge axs
	n = 25											# Number of datapoints to ax

	disguisedSignatures = distancesFile[distancesFile.QuestionedSignature.isin(disguised)]
	genuineSignatures = distancesFile[distancesFile.QuestionedSignature.isin(genuine)]
	forgedSignatures = distancesFile[~distancesFile.QuestionedSignature.isin(disguised)]
	forgedSignatures = forgedSignatures[~forgedSignatures.QuestionedSignature.isin(genuine)]

	print("Number of Disguised Entries\t", len(disguisedSignatures))
	print("Number of Genuine Entries\t", len(genuineSignatures))
	print("Number of Forged Entries\t", len(forgedSignatures))

	disguised_x = disguisedSignatures['ReferenceSignature'] + disguisedSignatures['QuestionedSignature']
	genuine_x = genuineSignatures['ReferenceSignature'] + genuineSignatures['QuestionedSignature']
	forged_x = forgedSignatures['ReferenceSignature'] + forgedSignatures['QuestionedSignature']

	disguised_x = disguised_x[:n]
	genuine_x = genuine_x[:n]
	forged_x = forged_x[:n]

	fig = plt.figure()

	for title in titles:
		print(title)
		disguised_y = disguisedSignatures[title][:n]
		genuine_y = genuineSignatures[title][:n]
		forged_y = forgedSignatures[title][:n]

		plt.scatter(disguised_x, disguised_y, c="blue", label="Disguised")
		plt.scatter(genuine_x, genuine_y, c="green", label="Genuine")
		plt.scatter(forged_x, forged_y, c="red", label="Forged")

		plt.title(title.upper())
		plt.xticks(rotation=90)
		plt.savefig("../Plots/" + title + ".png")
		plt.legend(fontsize='small')
		plt.show()

if __name__ == '__main__':
	main()