# Chatbot

## 📌 Description

This repository contains a simple **Python-based chatbot** built using machine learning techniques.  
It uses a set of predefined intents and responses to interact with users and can be trained to recognize patterns in text.

The project includes:
- Chatbot model training script
- Trained model and supporting files
- Main chatbot application

---

## 📁 Repository Contents

- `chatbot.py` – Main chatbot application  
- `train_chatbot.py` – Script to train the chatbot model  
- `intents.json` – List of user intents and responses  
- `model.pkl` – Trained chatbot model  
- `vectorizer.pkl` – Text vectorizer for transforming input text  
- `responses.pkl` – Encoded response data  
- `README.md` – Project documentation  

---

## 🧠 Requirements

- Python 3.7 or above  
- `pip` (Python package manager)

---

## 🛠️ How to Run

### Option 1: Run Pre-trained Chatbot

1. Clone the repository:
   ```bash
   git clone https://github.com/Akshu-1106/Chatbot.git
2. Navigate to the project directory:
   '''bash
   cd Chatbot
3. Install dependencies:
   '''bash
   pip install -r requirements.txt
(If requirements.txt doesn’t exist, install packages manually like numpy, scikit-learn, nltk, etc.)
4. Run the chatbot:
   '''bash
   python chatbot.py
5. Interact with the chatbot in the terminal.
### Option 2: Re-train the Model
1. Follow steps 1–3 above.
2. Run the training script:
   '''bash
   python train_chatbot.py
3. This will re-generate model files (model.pkl, vectorizer.pkl).

---

### 🧪 Usage
1. Launch the chatbot using python chatbot.py
2. Type messages to interact
3. The bot matches your input with intents in intents.json and replies accordingly

---

### 🤖 How It Works
1. The chatbot reads the intents from intents.json
2. Text input is vectorized using a text vectorizer
3. A trained ML model predicts the user intent
4. The bot responds with a matching response

---

### Project Status
✅ Completed— The project is finished and working as intended.
