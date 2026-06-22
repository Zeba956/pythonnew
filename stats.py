import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats #open source python library used for scientific, mathematical and more

#employee salaries 
salaries = [22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]

#central tendency -- where is the 'centre' of data?

mean = np.mean(salaries)
median = np.median(salaries)
mode = stats.mode(salaries,keepdims=True).mode[0]

print(f'Mean   (Average):       Rs.{mean:1f}K')
print(f'Median (Middle value):  Rs.{median}k')
print(f'Mode   (Most common):   Rs.{mode}K')






 
import numpy as np
salaries = [22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]
#spred - how varied is the date?
std = np.std(salaries)
var = np.var(salaries)
rng = max(salaries) - min(salaries)
q1 = np.percentile(salaries,25)
q3 = np.percentile(salaries,75)
iqr = q3-q1

print(f'Std Deviation: {std:2f}K (most important spread measure)')
print(f'IQR: {iqr}K (Q1={q1},Q3={q3})')

#outlier detection using IQR (interquartile range)

lower = q1 - 1.5*iqr
upper = q3 + 1.5*iqr
outliers = [x for x in salaries if x< lower or x > upper]
print(f'Outliers: {outliers}') 





#Correlation for Ai/Ml

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats

#Data
np.random.seed(42)
study = np.random.uniform(2,10,60)
marks = study * + np.random.normal(0,10,60)
marks = np.clip(marks,30,100)
absent = 10 - study + np.random.normal(0,1,60)

df = pd.DataFrame({'Study_Hours': study,'Marks':marks,'Absences':absent})

corr_matrix = df.corr()
print(corr_matrix.round(3))

plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f')
plt.title('Correlation Matrix');
plt.show()


#Pearson Correlation
r, p_value = stats.pearsonr(study, marks)
print(f'Study-Marks correlation: r={r:.3f}, p={p_value:.4f}')
print('Interpretation:','Strong positive' if r>0.7 else 'Moderate' if r>0.4 else 'Weak')






#Probability
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm    #normal distribution calculator


#you feed it a mean and standard deviation and it can answer any probability question about that distribution

#Normal Distribution -- the Bell Curve
#normal distribution with mean 165cm and standard deviation 7cm



mean_h, std_h = 165,7

#probability of being taller than 175cm
prob = 1- norm.cdf(175,mean_h,std_h)
print(f'P(height > 175cm) = {prob:.4f} = {prob*100:.1f}%')

print(f'68% of people: {mean_h-std_h:.0f}cm to {mean_h+std_h:.0f}cm')
print(f'95% of people: {mean_h-2*std_h:.0f}cm to {mean_h+2*std_h:.0f}cm')
print(f'99.7% of people: {mean_h-3*std_h:.0f}cm to {mean_h+3*std_h:.0f}cm')






from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np

# Simulated dataset: 500 student records
X = np.random.rand(500, 5)      # 5 features (study hrs, attendance, etc.)
y = np.random.randint(0, 2, 500) # Labels: pass(1)/fail(0)

# 80/20 Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f'Training samples: {len(X_train)} | Test samples: {len(X_test)}')

# 5-Fold Cross-Validation – more reliable than single split
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=50, random_state=42)

cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

print(f'CV scores each fold: {cv_scores.round(3)}')
print(f'Mean: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}')








import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Data
n_A, conv_A = 1000, 52
n_B, conv_B = 1000, 68

rate_A = conv_A / n_A
rate_B = conv_B / n_B

print(f'Version A conversion rate: {rate_A*100:.1f}%')
print(f'Version B conversion rate: {rate_B*100:.1f}%')
print(f'Improvement: {(rate_B-rate_A)/rate_A*100:.1f}%')

# Chi-square test
table = [[conv_A, n_A-conv_A],
         [conv_B, n_B-conv_B]]

chi2, p_value, dof, expected = stats.chi2_contingency(table)

print(f'Chi square: {chi2:.4f}')
print(f'P-value: {p_value:.4f}')
print('Result:',
      'SIGNIFICANT - B is better!'
      if p_value < 0.05
      else 'NOT significant -- could be random')






import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Study hours vs exam marks
study = [1,2,3,4,5,6,7,8,9,10,2.5,4.5,6.5,8.5]
marks = [25,38,52,65,71,85,89,93,96,43,68,82,91,98]

X = np.array(study).reshape(-1,1)
y = np.array(marks)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

print(f'Slope: {model.coef_[0]:.2f} (marks increase per study hour)')
print(f'Intercept: {model.intercept_:.2f} (marks at 0 study hours)')

y_pred = model.predict(X_test)

print(f'R² Score: {r2_score(y_test,y_pred):.4f} (1.0 = perfect!)')
print(f'RMSE: {mean_squared_error(y_test,y_pred)**0.5:.2f} marks average error')

# Predict new student
new_pred = model.predict([[7]])[0]
print(f'Student studying 7 hrs predicted marks: {new_pred:.1f}')

# Plot
plt.figure(figsize=(9,5))
plt.scatter(X,y,color='steelblue',s=100,alpha=0.8,label='Actual')
plt.plot(X,model.predict(X),color='red',linewidth=2,label='Predicted line')
plt.xlabel('Study Hours/Day')
plt.ylabel('Exam Marks')
plt.title('Linear Regression - Study Hours vs Marks')
plt.legend()
plt.grid(True,alpha=0.3)
plt.show()





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