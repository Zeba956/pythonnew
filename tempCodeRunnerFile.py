

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
print('TF-IDF shape:', matrix.shape)
print('Feature names:', tfidf.get_feature_names_out())