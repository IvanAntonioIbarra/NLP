import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

if __name__ == '__main__':
	
	stopwords = ['los','al']

	sentence = "Los niños están jugando al tenis"

	#Tokenization
	tokens = sentence.split(" ")

	#sentecne cleaning
	clean_tokens = []

	for token in tokens:
		if all(char in set(string.punctuation) for char in token):
			continue

		if token.isdigit():
			continue

		token = token.lower()
		token = token.strip()

		if token in stopwords:
			continue
	
		clean_tokens.append(token)

	print("Tokens:")
	print(tokens)
	print("Clean Tokens:")
	print(clean_tokens)

	# only for this practice
	temp = []
	temp.append(' '.join(clean_tokens))
	
	print("Clean Tokens united:")
	print(temp)

	#bag of words transformation
	count_vect = CountVectorizer()
	bag_of_words_array = count_vect.fit_transform(temp)

	#model training
	naive_bayes_classifier = MultinomialNB()
	naive_bayes_classifier.fit(bag_of_words_array,['1'])

	#model predict
	print("Predict...")
	print(naive_bayes_classifier.predict(bag_of_words_array))

	"""
	Implementar 3 oraciones 

	"""

