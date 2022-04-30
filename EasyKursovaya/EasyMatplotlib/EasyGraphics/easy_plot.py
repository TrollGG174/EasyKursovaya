import matplotlib.pyplot as plt
import numpy as np

'''
Пример создания графика линии 
'''

x = np.linspace(-5, 5, 100)
y = np.cos(x)
fig, ax = plt.subplots()
ax.plot(x, y,
        linestyle = '-',
        linewidth = 1,
        color = 'red')
ax.plot(x, y + 1,
        linestyle = '--',
        linewidth = 2,
        color = 'green')
ax.plot(x, y + 2,
        linestyle = '-.',
        linewidth = 4,
        color = 'blue')
ax.plot(x, y + 3,
        linestyle = ':',
        linewidth = 6,
        color = 'pink')
plt.show()