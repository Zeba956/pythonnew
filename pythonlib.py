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
