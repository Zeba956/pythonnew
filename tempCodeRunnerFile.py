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

sns.boxplot(data=df, x='city', y='marks', palette='Set2')
plt.title('Marks Distribution by City')
plt.show()

