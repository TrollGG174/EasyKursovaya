import matplotlib.pyplot as plt
import numpy as np

'''
Пример создания кругового графика 
'''

x = np.arange(0, 9)
fig, ax = plt.subplots()
ax.pie(x)
plt.show()