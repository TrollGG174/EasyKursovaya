import numpy as np
import matplotlib.pyplot as plt

'''
Пример построения графика нормального распределения и добавления функций с помощью LaTeX

'''

a, sigma = 1.3, 2.9
data = np.random.normal(a, sigma, 10000)
fig, ax = plt.subplots()
ax.hist(data, bins=50, rwidth=0.4)
ax.set_title(r'$p(x)=\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}}$', fontsize=14, pad=20)
plt.show()