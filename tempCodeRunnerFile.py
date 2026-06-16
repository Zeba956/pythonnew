
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