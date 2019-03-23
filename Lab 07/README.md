# Lab 07: Sentiment Analysis (Part 1)

## Libraries Needed
- pandas
- BeautifulSoup
- re (Regular Expressions)
- nltk (Natural Language Toolkit)

## Task
Write a function that does the following Steps on `labeledTrainData.tsv` (which contains 25000 IMDB movie reviews). Run the function for each review in your training data and store the output in one list.
1. Remove HTML
2. Remove non letters
3. Convert to lowercase and split it into words
4. Remove stops words
5. Joint back and return the joined sentence