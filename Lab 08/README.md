# Lab 08: Sentiment Analysis (Part 2)

## Task
In the previous section, you learnt how to train a Naïve Bayes classifier. Your lab task is to train a Naïve Bayes’ classifier using IMDB movie reviews (25000 movie reviews). Remember to clean the reviews before building bag of word representation. You can either use the function you wrote in the last lab to clean the reviews or use review_to_words.py.
In the IMDB data, we have a very large number of reviews, which will give us a large vocabulary. To limit the size of the feature vectors, we should choose some maximum vocabulary size. You can start with 5000 most frequent words
```
vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, stop_words = None, max_features = 5000)
```
Partition the 25000 movie reviews into training (80%) and validation set (20%). Train on 80% reviews and then report accuracy on the remaining 20%.

|Vocabulary Size|Alpha (Laplace Smoothing)|Accuracy on 20% validation set|
|--|--|--|
|3000|0.00001|78.83333333333333 %|
|3000|5|82.33333333333334 %|
|5000|0.00001|82.69999999999999 %|
|5000|5|83.2 %|