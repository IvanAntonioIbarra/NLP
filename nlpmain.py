import string
from sklearn.feature_extraction_text import CountVectorizer
from sklearn.niave_bayes import MultinomialNB

if __name__ == 'main':
  sentence = "Se dirigió sin dilación hacia el fondo de la cueva Encontró un hueso de gamo. Todavía tenía algo de carne adherida. Empezó a triturarlo confruición"

  #tokenizar
  tokens = sentence.split(' ')

  #sentence cleaning

  clean_token=[]

  for token in tokens:

    #remove punctuation
    if all(char in set(string.punctuation) for char in token):
      continue

    #remove numbers
    if token.isdigit():
      continue

    #transform the token to lowcase and remove sentences
    token= token.lower()
    token = token.strip()

    #remove stopworld 
    if token in stopwords:
      continue
    clean_token.append(token)

  print(tokens)
  print(clean_token)
