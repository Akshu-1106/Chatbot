import json
import nltk
import random
import pickle
import numpy as np

from nltk.stem import WordNetLemmatizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load intents
with open("intents.json") as file:
    data = json.load(file)

corpus = []
labels = []
responses = {}

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = pattern.lower().split()
        tokens = [lemmatizer.lemmatize(word) for word in tokens]
        corpus.append(" ".join(tokens))
        labels.append(intent["tag"])
    responses[intent["tag"]] = intent["responses"]

# Vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Save model and data
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
pickle.dump(responses, open("responses.pkl", "wb"))

print("✅ Chatbot trained successfully!")
