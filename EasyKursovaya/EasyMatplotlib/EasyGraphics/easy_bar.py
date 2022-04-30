import numpy as np
import matplotlib.pyplot as plt

'''
Пример создания гистограммы 
'''

x = np.arange(1, 9)
y = np.random.randint(1, 20, size=8)
fig, ax = plt.subplots()
ax.bar(x, y)
plt.show()