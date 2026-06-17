

 
import numpy as np
salaries = [22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]
#spred - how varied is the date?
std = np.std(salaries)
var = np.var(salaries)
rng = max(salaries) - min(salaries)
q1 = np.percentile(salaries,25)
q3 = np.percentile(salaries,75)
iqr = q3-q1

print(f'Std Deviation: {std:2f}K (most important spread measure)')
print(f'IQR: {iqr}K (Q1={q1},Q3={q3})')

#outlier detection using IQR (interquartile range)

lower = q1 - 1.5*iqr
upper = q3 + 1.5*iqr
outliers = [x for x in salaries if x< lower or x > upper]
print(f'Outliers: {outliers}') 