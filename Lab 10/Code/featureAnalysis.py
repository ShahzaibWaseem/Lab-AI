import cv2
import matplotlib.pyplot as plt
import pandas as pd

disguised = ["Q006", "Q015", "Q028", "Q029", "Q034", "Q087", "Q090"]
titles = ['Centroids', 'Transitions', 'Ratios', 'BlackPixels', 'Normalized', 'Angles', 'NormalizedBlacks']

def main():
	n = 100										# Number of datapoints to plot
	distancesFile = pd.read_csv("../Text/distances.csv")
	distancesFile = distancesFile.sample(frac=1)
	distancesFile = distancesFile[~distancesFile.QuestionedSignature.isin(disguised)]

	x = distancesFile['ReferenceSignature'] + distancesFile['QuestionedSignature']
	x = x[:n]

	plt.rcParams["figure.figsize"] = [22, 15]	# Enlarge Plots

	for title in titles:
		y = distancesFile[title][:n]

		plt.scatter(x, y)
		plt.title(title.upper())
		plt.xticks(rotation=90)
		plt.savefig("../Plots/" + title + ".png")
		plt.show()

if __name__ == '__main__':
	main()