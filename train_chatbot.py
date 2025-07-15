import json
import random
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load JSON
with open('intents.json') as file:
    data = json.load(file)

corpus = []
xy = []

# Prepare training data
for intent in data['intents']:
    for pattern in intent['patterns']:
        tokens = nltk.word_tokenize(pattern)
        tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
        sentence = " ".join(tokens)
        corpus.append(sentence)
        xy.append((sentence, intent['tag']))

# Vectorize
vectorizer = CountVectorizer()
X = vectorizer.fit_transform([x for x, y in xy])
y = [y for x, y in xy]

# Train model
model = SVC(kernel='linear')
model.fit(X, y)

# Save model and vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
