






import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Dataset
data = {
    'Study_Hours': [1,2,3,4,5,6,7,8,9,10],
    'Marks': [25,35,45,50,60,70,75,85,90,95]
}

df = pd.DataFrame(data)

# Features and Target
X = df[['Study_Hours']]
y = df['Marks']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LinearRegression()

# Training
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Predict marks for a student studying 7.5 hours
hours = [[7.5]]
predicted_marks = model.predict(hours)

print("\nPredicted Marks for 7.5 Study Hours:")
print(round(predicted_marks[0], 2))

# Graph
plt.figure(figsize=(8,5))

# Actual Data Points
plt.scatter(X, y, label="Actual Data")

# Regression Line
plt.plot(X, model.predict(X), linewidth=2, label="Regression Line")

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)

plt.show()