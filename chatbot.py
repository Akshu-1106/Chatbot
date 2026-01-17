import pickle
import nltk
import random
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load trained files
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
responses = pickle.load(open("responses.pkl", "rb"))

def preprocess(text):
    tokens = text.lower().split()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return " ".join(tokens)

print("🤖 Chatbot is running! (type 'exit' to stop)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    processed = preprocess(user_input)
    vector = vectorizer.transform([processed])
    prediction = model.predict(vector)[0]

    reply = random.choice(responses[prediction])
    print("Bot:", reply)
