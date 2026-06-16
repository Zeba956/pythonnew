#Scatter plot - relationship between two variable
import matplotlib.pyplot as plt
import numpy as np

study_hrs = np.random.uniform(2,10,50)
marks = study_hrs * 7 + np.random.normal(0,8,50)
marks = np.clip(marks,30,100)

plt.figure(figsize=(8,5))
plt.scatter(study_hrs,marks, c=marks, cmap='RdYlGn', s=100, alpha=0.8)
plt.colorbar(label='Marks')
plt.title('Study Hours vs Exam Marks')
plt.xlabel('Study Hours/Day')
plt.ylabel('Exam Marks')
plt.show()