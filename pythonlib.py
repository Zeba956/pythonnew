#Numpy
#Pandas
import numpy as np
arr1d = np.array([1,2,3,4,5])
arr2d = np.array([[85,90,78],[72,88,95],[91,76,83]])

print(arr2d.shape)
print(arr2d.dtype)
print(arr2d.ndim)





import pandas as pd

# Create DataFrame
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha'],
    'Marks': [85, 92, 73, 88],
    'City': ['Bhopal', 'Indore', 'Jabalpur', 'Bhopal']
}

df = pd.DataFrame(data)

# # Select columns
# print("df['Name']:\n", df['Name'])
# print("\nName and Marks columns:")
# print(df[['Name', 'Marks']])

# # Filter rows
# print("\nStudents with Marks >= 85:")
# print(df[df['Marks'] >= 85])

# print("\nStudents from Bhopal:")
# print(df[df['City'] == 'Bhopal'])
# print(df[(df['Marks'] >= 80) & (df['City'] == 'Indore')])

# def get_grade(x):
#     if x >= 90:
#         return 'A'
#     elif x >= 75:
#         return 'B'
#     else:
#         return 'C'
    
# df['Grade'] = df['Marks'].apply(get_grade)
# print(df['Grade'])
# print("-----------")
# print(df)



#GroupBy -- like Excel Pivot
city_avg = df.groupby('City')['Marks'].mean()
print(city_avg)




#read real csv file
df2 = pd.read_csv('students.csv')
#cleaning
df2.to_csv('clean_output.csv',index = False)




#unclean data to clean data
import csv

records = [
    ['Name','Marks','City','Grade'],
    ['Rahul','#85','BhopalCity','B*'],
    ['Priya','#92','IndoreDist','@A'],
    ['Amit','#73','JabalpurCity','B']
]

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(records)

print("Unclean data created successfully!")





import pandas as pd

# CSV file read karo
df = pd.read_csv("students.csv")

print("Unclean Data:")
print(df)

df["Name"] = df["Name"].str


# Marks se # remove karo
df["Marks"] = df["Marks"].str.replace("#", "", regex=False)
df["Marks"] = pd.to_numeric(df["Marks"])

# City se City aur Dist remove karo
df["City"] = df["City"].str.replace("City", "", regex=False)
df["City"] = df["City"].str.replace("Dist", "", regex=False)

# Grade se @ aur * remove karo
df["Grade"] = df["Grade"].str.replace("@", "", regex=False)
df["Grade"] = df["Grade"].str.replace("*", "", regex=False)

print("\nCleaned Data:")
print(df)

# Cleaned data save karo
df.to_csv("clean_output.csv", index=False)

print("\nData cleaned and saved to clean_output.csv")




#Matplotlib
import matplotlib.pyplot as plt

months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec']
sales = [45,52,48,61,58,72,69,75,68,82,90,95]

#Line Chart - trends over time
plt.figure(figsize=(12,5))
plt.plot(months,sales,marker='o',color='steelblue',linewidth=2,markersize=8)
plt.fill_between(months,sales,sales,alpha=0.15,color='steelblue')
plt.title('Monthly Sales 2024 (Rs. Thousands)', fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Sales (Rs. k)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()




#Bar graph data
import matplotlib.pyplot as plt

cities = ['Bhopal','Indore','Jabalpur','Gwalior','Ujjain']
students = [1200, 2800, 980, 850, 650]
colors = ['#2196F3','#4CAF50','#FF9800','#9C27B0','#F44336']

#Bar Chart - comparing categories
plt.figure(figsize=(9,5))
bars = plt.bar(cities, students, color=colors, edgecolor='white',linewidth=1.5)
plt.title('Students Enrolled per City')
plt.ylabel('Number of Students')
plt.xlabel('Cities')
for bar,val in zip(bars,students):
    plt.text(bar.get_x()+bar.get_width()/2, val+30, str(val), ha='center',fontweight='bold')
plt.tight_layout()
plt.show()



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





#Seaborn Library

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

#Histogram with KDE -- see the distribution
plt.figure(figsize=(10,4))
sns.histplot(df['marks'],bins=20, kde=True, color='steelblue')
plt.title('Distribution of Student Marks')
plt.show()




#17-06-2026
#box gragh using seaborn


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
sns.heatmap(df[['marks','study_hours']].corr(),annot=True,cmap='coolwarm',vmin=-1,vmax=1)
plt.title('Correlation Matrix')
plt.show()











