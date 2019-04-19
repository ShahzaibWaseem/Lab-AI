import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import re
import nltk
# nltk.download("stopwords")
from nltk.corpus import stopwords
import sklearn
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def review_to_words(raw_review):
	review_without_html = re.sub(r'<[^<>]+>', "", raw_review)				# remove HTML Tags
	review_with_alphabets = re.sub(r'[^a-zA-Z]', " ", review_without_html)	# remove non-alphabets

	words = review_with_alphabets.lower().split()							# lower and words
	stops = set(stopwords.words("english"))
	words = [w for w in words if not w in stops]							# remove stop words

	clean_review = " ".join(words)
	return clean_review

def main():
	sizeofdata=5000
	vectorizer = CountVectorizer(analyzer = "word", \
	tokenizer = None, \
	preprocessor = None, \
	stop_words = None, \
	max_features = 5000)

	test = pd.read_csv("labeledTrainData.tsv", header=0, delimiter="\t", quoting=3)

	num_reviews = len(test["review"])
	clean_test_reviews = []
	y=[]
	print("Cleaning and parsing the test set movie reviews...\n")

	for i in range(0,sizeofdata):
		clean_review = review_to_words(test["review"][i])
		clean_test_reviews.append(clean_review)
		y.append(test["sentiment"][i])

	test_data_features = vectorizer.fit_transform(clean_test_reviews)
	test_data_features = test_data_features.toarray()
	y=np.array(y)

	x_train, x_test, y_train, y_test=sklearn.model_selection.train_test_split(test_data_features,y,test_size=0.20,random_state=0)

	clf = MultinomialNB(alpha=0.00001)
	clf.fit(x_train,y_train)
	y_pred_class=clf.predict(x_test)
	accuracy=metrics.accuracy_score(y_test, y_pred_class)

	print("Accuracy of the classifier =",100*accuracy,"%")

if __name__ == '__main__':
	main()