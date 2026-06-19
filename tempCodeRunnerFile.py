

import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt

#data
n_A, conv_A = 1000, 52
n_B, conv_B = 1000, 68
rate_A = conv_A / n_A
rate_B = conv_B / n_B

print(f'Version A conversion rate: {rate_A*100:.1f}%')
print(f'Version B conversion rate: {rate_B*100:.1f}%')
print(f'Improvement: {(rate_B-rate_A)/rate_A*100:.1f}%')