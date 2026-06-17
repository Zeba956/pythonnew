import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(42)

#data
df = pd.DataFrame({
    'marks':       np.random.randint(40,100,100),
    'study_hours': np.random.uniform(2,10,100),
    'city':        np.random.choice(['Bhopal','Indore','Jabalpur'],100),
    'gender':      np.random.choice(['Male','Female'],100)
})

#Correlation Heatmap Graph_ critical in data science
plt.figure(figsize=(5,4))
sns.heatmap(df[['marks','study_hours']].corr(),annot=True,cmap='pink',vmin=-1,vmax=1)
plt.title('Correlation Matrix')
plt.show()