# AI Chatbot with NLP

COMPANY: CODTECH IT SOLUTIONS

NAME: TANVI BEJADI

INTERN ID: CT04DH2184

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

Project Description:
This project is about creating a simple AI chatbot using Python and Natural Language Processing (NLP). The chatbot is designed to respond to the user’s questions based on predefined answers. It understands basic user input, matches it to a category (called an "intent"), and gives a suitable response. The chatbot is trained to recognize common words and phrases and reply accordingly.

The chatbot was built using Python 3.11 and developed in Visual Studio Code (VS Code). This is a free code editor that supports Python and makes it easier to write, edit, and test code. The program was tested on Windows 10 using Command Prompt.

We used a few important Python libraries in this project:

NLTK (Natural Language Toolkit): This library helps in breaking down user messages into words and converting them into simpler forms (called tokenization and lemmatization). This is useful for understanding what the user is saying.

Scikit-learn: This is a machine learning library used to train a model. It converts words into numbers using TfidfVectorizer and then uses SVC (Support Vector Classifier) to learn and predict the category of the user message.

Pickle: This module saves the trained model and vectorizer into files (model.pkl and vectorizer.pkl) so that we can use them later without retraining every time.

JSON: The chatbot reads its question-and-answer data from a file called intents.json. This file contains user messages (patterns), the related category (intent), and the responses.

Working Procedure:
Data Preparation:
First, we define a JSON file (intents.json) where we list different types of questions users may ask. For each type, we provide example sentences and possible responses.

Training the Model (train_chatbot.py):

The script reads the JSON file.

It processes the example questions using NLTK (tokenization and lemmatization).

It converts these words into numerical form using TfidfVectorizer.

It trains the machine learning model (SVC) to recognize different types of questions.

The trained model and vectorizer are saved as .pkl files.

Running the Chatbot (chatbot.py):

The chatbot loads the trained model and vectorizer.

It takes user input from the keyboard.

It processes the input and predicts the most likely category.

Based on the prediction, it selects and shows a response from the related intent.

The chat continues until the user types ‘quit’.

Applications:
This chatbot can be used in many fields:

Customer Support: Answering frequently asked questions automatically.

Education: Helping students with their questions.

Healthcare: Giving general advice or appointment details.

Banking: Answering common account or transaction questions.

Online Shopping: Helping customers with order tracking or product information.

Conclusion:
This project is a good example of how Natural Language Processing and machine learning can be used to build a simple but useful chatbot. The chatbot understands user messages and responds smartly using predefined data. It can be improved further by adding more types of questions, better responses, or using a web interface. This project gives a strong base for learning about AI, NLP, and chatbot systems.

#OUTPUT

<img width="397" height="187" alt="Image" src="https://github.com/user-attachments/assets/33a3f458-a57c-4751-bc77-7845a13be66a" />
