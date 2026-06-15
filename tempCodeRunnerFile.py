
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