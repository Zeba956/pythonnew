

# Machine learning Classification
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Dataset
data = {
    'Study_Hours': [1,2,3,4,5,6,7,8,9,10,2.5,4.5,6.5,8.5],
    'Pass': [0,0,0,0,1,1,1,1,1,1,0,1,1,1]
}

df = pd.DataFrame(data)

# Features and Target
X = df[['Study_Hours']]
y = df['Pass']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LogisticRegression()

# Training
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", round(accuracy * 100, 2), "%")

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# New Student Prediction
hours = [[7]]
prediction = model.predict(hours)

print("\nPrediction for 7 study hours:")

if prediction[0] == 1:
    print("Pass")
else:
    print("Fail")

# Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df['Study_Hours'], df['Pass'])

plt.title("Student Pass/Fail Classification")
plt.xlabel("Study Hours")
plt.ylabel("Result")

plt.yticks([0,1], ["Fail", "Pass"])
plt.grid(True)

plt.show()