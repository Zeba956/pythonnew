


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
