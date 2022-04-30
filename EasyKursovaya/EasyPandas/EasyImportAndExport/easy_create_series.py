import pandas as pd

'''
Создание объекта Series
'''

s = pd.Series({'first_element': 1,
               'second_element': 2.1,
               'third_element': 2},
              dtype='float64')

print(s)

