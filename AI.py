print("Hello AI")


#epochs 
#backpropagration



#25-06-2026
#Neural Learning
#Xor problem


import numpy as np

def sigmoid(x): return 1 / (1+np.exp(-x))
def sigmoid_d(x): return x * (1-x)

X = np.array ([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

np.random.seed(42)
W1 = np.random.randn(2,4) * 0.5
W2 = np.random.randn(4,1) * 0.5

lr = 0.5
losses = []

for epoch in range(10000):
    h = sigmoid(X @ W1)
    o = sigmoid(h @ W2)

    loss = np.mean((y-o)**2)
    losses.append(loss)

    d_o = (o-y) * sigmoid_d(o)
    d_h = (d_o @ W2.T) * sigmoid_d(h)


    W2 -= lr * h.T @ d_o
    W1 -= lr * X.T @ d_h

import matplotlib.pyplot as plt
plt.plot(losses); plt.title('Loss Decreasing During Training')
plt.xlabel('Epoch'); plt.ylabel('Loss'); plt.show()


print('Final predictions (should be close to [0,1,1,0]):')
print(np.round(o,2))






import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt





#26-06-2026
#NLP (Natural language processing) and Gen Ai

# pip install nltk scikit-learn

# python -m pip install nltk scikit-learn

# python3 -m pip install nltk scikit-learn







#27-06-2026

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Required datasets download
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')   # Newer NLTK versions ke liye

# Input text
text = "Students are learning Python for AI and Machine Learning in Bhopal!"

# Step 1: Tokenization - sentence ko words me todna
tokens = word_tokenize(text.lower())
print("Tokens:", tokens)

# Step 2: Stopwords remove karna
stop = set(stopwords.words('english'))
filtered = [w for w in tokens if w not in stop and w.isalpha()]
print("After stopword removal:", filtered)

# Step 3: Lemmatization - word ko root form me convert karna
lemma = WordNetLemmatizer()
final = [lemma.lemmatize(w) for w in filtered]
print("After lemmatization:", final)



# TF-IDF - convert text to numbers for ML
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    'Python is great for data science',
    'Machine learning is amazing',
    'AI is the future of technology'
]

tfidf = TfidfVectorizer()
matrix = tfidf.fit_transform(docs)
print('TF-IDF shape:', matrix.shape)  #(3 docs, N unique words)
print('Feature names:', tfidf.get_feature_names_out())
