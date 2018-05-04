import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

if __name__ == '__main__':

	"""
	Tarea Inteligencia Artificial
	"""

	#Palabras a quitar de la oracion o indeseadas
	stopwords = ['los','al', 'siempre', 'el', 'y', 'muchacho', 'tomo', 'la', 'decicion', 'empesar', 'logro', 'de', 'lo', 'logro', 'las', 'si','cualquier', 'de']
	#Oracion de la que se desea aprender
	sentences = ["Las tareas de inteligencia artificial siempre estan padres", "La Universidad de Stanford elabora las preguntas, para probar si cualquier modelo de machine-learning es capaz de procesar grandes niveles de información, antes de proporcionarles las respuestas.", "Cuando el muchacho tomo la decicion de empesar y emepezo su estudio y lo logro fue cuando saco buenas calificaciones"]
	temp = []

	for sentence in sentences:
		print("sentencias: "+sentence)
		tokens = sentence.split(" ")
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
		 
		temp.append(' '.join(clean_tokens))
	
	#bag of words transformation
	count_vect = CountVectorizer()
	bag_of_words_array = count_vect.fit_transform(temp)

	#model training
	naive_bayes_classifier = MultinomialNB()
	naive_bayes_classifier.fit(bag_of_words_array,['Tarea IA','Universidad','Estudioso'])

	"""
	Oraciones1 a predecir
	"""

	# sentenceToPredict = 'Cuando el muchacho estudio'
	# print(sentenceToPredict)
	# sentenceToPredict = 'La Universidad de Stanford'
	# print(sentenceToPredict)

	
	sentenceToPredict = 'la tarea de inteligencia artificial esta padre'
	print(sentenceToPredict)
	tokensP = sentenceToPredict.split(" ")
	temp2 = []
	clean_tokensP = []

	for tokenF in tokensP:
			if all(char in set(string.punctuation) for char in token):
		 		continue

			if tokenF.isdigit():
				continue

			tokenP = tokenF.lower()
			tokenP = tokenF.strip()
			if tokenP in stopwords:
				continue

			clean_tokensP.append(tokenP)
		 
	temp2.append(' '.join(clean_tokensP))
	bag_of_words_array = count_vect.transform(temp2)
	print(bag_of_words_array)
	print(naive_bayes_classifier.predict(bag_of_words_array))