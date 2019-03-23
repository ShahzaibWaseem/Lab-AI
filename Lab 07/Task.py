import pandas as pd
from bs4 import BeautifulSoup
import re
import nltk
# nltk.download("stopwords")
from nltk.corpus import stopwords

def reviewToWords(raw_review):
	review_without_html = re.sub(r'<[^<>]+>', "", raw_review)				# remove HTML Tags
	review_with_alphabets = re.sub(r'[^a-zA-Z]', " ", review_without_html)	# remove non-alphabets

	words = review_with_alphabets.lower().split()							# lower and words
	stops = set(stopwords.words("english"))
	words = [w for w in words if not w in stops]							# remove stop words

	clean_review = " ".join(words)
	return clean_review

train = pd.read_csv('labeledTrainData.tsv', header=0, delimiter='\t', quoting=3)
reviews = []

for review in train['review']:
	clean_review = reviewToWords(review)
	reviews.append(clean_review)

print(len(reviews))