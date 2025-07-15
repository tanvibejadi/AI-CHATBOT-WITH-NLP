# AI Chatbot with NLP

COMPANY: CODTECH IT SOLUTIONS

NAME: TANVI BEJADI

INTERN ID: CT04DH2184

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

Project Description:
This project involves the design and implementation of a rule-based AI chatbot using Natural Language Processing (NLP) techniques in Python. The chatbot is capable of answering user queries based on a set of predefined intents. It demonstrates the integration of text preprocessing, machine learning classification, and interaction handling to simulate an intelligent conversational system. The chatbot processes natural language inputs, classifies them into categories (intents), and responds accordingly.

The chatbot system was built using Python 3.11, a popular programming language for artificial intelligence and data science projects due to its simplicity and extensive library support. The development and execution of the code were carried out in the Visual Studio Code (VS Code) editor, which provided features such as integrated terminal, syntax highlighting, and debugging tools. All scripts were tested and run using the Windows 10 operating system through the Command Prompt.

Tools and Technologies Used:
Several Python libraries and tools were used in this project:

NLTK (Natural Language Toolkit): This is a leading platform for building Python programs to work with human language data. In this project, NLTK was used for tokenization and lemmatization of input text. These processes helped convert user queries into standardized forms that the model could interpret effectively.

Scikit-learn: This machine learning library was used for training the classification model. Specifically, the TfidfVectorizer was used to convert textual data into numerical feature vectors, and the SVC (Support Vector Classifier) was employed as the machine learning algorithm to classify input queries into the appropriate intent categories.

Pickle: This Python module was used for object serialization. The trained model and vectorizer were saved to disk using Pickle so they could be reused later without retraining.

JSON: The intents.json file contains the data the chatbot uses to understand user input. It defines the intent tags, associated patterns (example queries), and responses for each category.

How It Works:
The chatbot project is composed of two main Python scripts: train_chatbot.py and chatbot.py. The train_chatbot.py script reads the intents from the JSON file, processes the text using NLTK, and trains a classifier using Scikit-learn. The resulting model and vectorizer are saved as model.pkl and vectorizer.pkl. The chatbot.py script loads these files and starts an interactive loop that allows users to enter queries and receive responses.

When a user inputs a message, the chatbot vectorizes the input using the same vectorizer used during training. The input is then classified using the trained model. Based on the predicted intent, a corresponding response is selected randomly from the predefined set.

Applications:
This chatbot model can be applied in various real-world scenarios, including:

Customer support services to handle frequently asked questions.

Educational platforms for answering student queries.

Healthcare services to provide general health advice or appointment information.

Banking and finance domains for responding to basic account-related questions.

E-commerce platforms for order tracking, product inquiries, and service support.

Conclusion:
In summary, this project provides a hands-on implementation of a simple rule-based chatbot using Python and NLP. It showcases how basic machine learning and language processing techniques can be combined to develop a functioning chatbot capable of understanding and responding to human input. The project can serve as a foundation for more advanced conversational agents incorporating deep learning, context handling, or web integration.

#OUTPUT

<img width="397" height="187" alt="Image" src="https://github.com/user-attachments/assets/33a3f458-a57c-4751-bc77-7845a13be66a" />
