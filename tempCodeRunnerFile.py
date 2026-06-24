
from xgboost import XGBClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd 

data = load_breast_cancer()
#print("Data:\n", data)
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state = 42)

xgb = XGBClassifier(n_estimators=100, max_depth=4, learning_rate=0.1,
                    random_state=42, eval_metric='logloss', verbosity=0)
xgb.fit(X_train,y_train)
print(f'XGBoost Accuracy: {accuracy_score(y_test,xgb.predict(X_test))*100:.2f}%')