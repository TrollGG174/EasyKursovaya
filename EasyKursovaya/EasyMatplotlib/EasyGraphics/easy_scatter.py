import numpy as np
import matplotlib.pyplot as plt

'''
Пример создания графика точек 
'''

x = np.random.rand(1000)
y = np.random.rand(1000)
fig, ax = plt.subplots()
ax.scatter(x, y, color='green')
ax.set_facecolor('black')
plt.show()