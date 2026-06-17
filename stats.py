import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats #open source python library used for scientific, mathematical and more

#employee salaries 
salaries = [22,28,35,42,38,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]

#central tendency -- where is the 'centre' of data?

mean = np.mean(salaries)
median = np.median(salaries)
mode = stats.mode(salaries,keepdims=True).mode[0]

print(f'Mean   (Average):       Rs.{mean:1f}K')
print(f'Median (Middle value):  Rs.{median}k')
print(f'Mode   (Most common):   Rs.{mode}K')