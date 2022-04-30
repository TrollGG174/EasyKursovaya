import matplotlib.pyplot as plt
import numpy as np

'''
Пример создания 3D графика
'''

x = np.linspace(-np.pi, np.pi, 50)
y = x
z = np.cos(x)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
plt.show()