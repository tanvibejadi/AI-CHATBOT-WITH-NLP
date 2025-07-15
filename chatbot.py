import pickle
import random
import nltk
from nltk.stem import WordNetLemmatizer
import json

lemmatizer = WordNetLemmatizer()

# Load model and data
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

with open('intents.json') as file:
    intents = json.load(file)

def preprocess_input(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
    return " ".join(tokens)

def get_response(user_input):
    inp = preprocess_input(user_input)
    X = vectorizer.transform([inp])
    intent = model.predict(X)[0]
    
    for intent_data in intents['intents']:
        if intent_data['tag'] == intent:
            return random.choice(intent_data['responses'])
    
    return "Sorry, I didn't understand that."

# Chat loop
print("Chatbot is running! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = get_response(user_input)
    print("Bot:", response)
