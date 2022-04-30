import matplotlib.pyplot as plt

'''
Основные функции 
'''

''' Взаимодействие Figure и Axes '''

# figure = plt.figure()
# axes = figure.add_subplot(111)

# figure.set(facecolor = 'pink')
# axes.set(facecolor = 'yellow',
#        xlim = [-10, 10],
#        ylim = [-2, 2],
#        title = 'EasyMatplotlib',
#        xlabel = 'ось абсцис (XAxis)',
#        ylabel = 'ось ординат (YAxis)')

''' Простейшие методы для отрисовки графиков '''

# figure = plt.figure()
# axes = figure.add_subplot()
# axes.plot([0, 5, 0, 5], [30, 30, 0, 0])
# axes.scatter([6, 7, 8, 9, 10], [30, 15, 0, 15, 30])

''' Вывод нескольких графиков в одной области '''

# figure = plt.figure()
# ax_1 = figure.add_subplot(2, 2, 1)
# ax_2 = figure.add_subplot(2, 2, 2)
# ax_3 = figure.add_subplot(2, 2, 3)
# ax_4 = figure.add_subplot(2, 2, 4)
#
# ax_1.set(title = '1', xticks=[0, 10], yticks=[0, 5])
# ax_2.set(title = '2', xticks=[0, 10], yticks=[0, 5])
# ax_3.set(title = '3', xticks=[0, 10], yticks=[0, 5])
# ax_4.set(title = '4', xticks=[0, 10], yticks=[0, 5])
#
# ax_1.plot([1, 3, 4, 5], [5, 3, 2, 4])
# ax_2.plot([1, 2, 7, 10], [1, 2, 4, 5])
# ax_3.plot([3, 4, 4, 9], [3, 1, 5, 0])
# ax_4.plot([10, 7, 5, 3], [0, 5, 3, 1])

''' Добавление стрелок '''

# figure = plt.figure()
# axes = figure.add_subplot()
# axes.plot([0, 4, 8, 10], [7, 4, 4, 10])
# axes.arrow(6, 7, 0, -2,
#          width = 0.15,
#          head_length = 1)

''' Создание легенды '''

# x = [0, 5, 20]
# y1 = [10, 13, 15]
# y2 = [8, 6, 10]
# y3 = [5, 3, 1]
# fig, ax = plt.subplots()
# ax.plot(x, y1, label='first')
# ax.plot(x, y2, label='second')
# ax.plot(x, y3, label='third')
# ax.legend(loc='lower left')

''' Добавление сетки '''

# figure = plt.figure()
# ax_1 = figure.add_subplot(211)
# ax_2 = figure.add_subplot(223)
# ax_3 = figure.add_subplot(224)
# ax_1.plot([1, 3, 5, 7, 9], [2, 5, 3, 5, 2])
# ax_2.plot([1, 3, 5, 7, 9], [2, 5, 3, 5, 2])
# ax_3.plot([1, 3, 5, 7, 9], [2, 5, 3, 5, 2])
# ax_1.grid(axis='both')
# ax_2.grid(axis='x')
# ax_3.grid(axis='y')

''' Добавление прямых '''

figure = plt.figure()
ax = figure.add_subplot()
x = [0, 5, 10, 15, 20]
y = [10, 5, 7, 5, 10]
ax.plot(x, y)
ax.vlines(10, 5, 7, color='r')
ax.vlines(5, 5, 10, color='r')
ax.vlines(15, 5, 10, color='r')
ax.hlines(7, 2.5, 17.5, color='black')
ax.hlines(5, 0, 20, color='black')

plt.show()