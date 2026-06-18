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




