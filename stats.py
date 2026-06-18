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




