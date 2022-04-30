import pandas as pd
import numpy as np

'''
Работа со статистическими функциями
'''

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df1 = pd.DataFrame(np.random.randint(0,50,size=(500, 4)), columns=list('ABCD'))

''' Получение объема выборки '''
# print("df1.count()")
# print(df1.count())

''' Получение уникальных значений в выборке '''
# print("df1['A'].unique()")
# print(df1['A'].unique())

''' Получение количества уникальных значений в выборке '''
# print("df1['A'].nunique()")
# print(df1['A'].nunique())

''' Получение уникальных значений в выборке и их количества '''
# print("df1['A'].value_counts()")
# print(df1['A'].value_counts())

''' Получение минимального значения в выборке '''
# print("df1['A'].min()")
# print(df1['A'].min())

''' Получение максимального значения в выборке '''
# print("df1['A'].max()")
# print(df1['A'].max())

''' Получение основных статистик '''
# print("df1.describe()")
# print(df1.describe())

''' Получение среднего '''
# print("df1['A'].mean()")
# print(df1['A'].mean())

''' Получение медианы '''
# print("df1['A'].median()")
# print(df1['A'].median())

''' Получение моды '''
# print("df1['A'].mode()")
# print(df1['A'].mode())

''' Получение дисперсии '''
# print("df1['A'].var()")
# print(df1['A'].var())

''' Получение стандартного отклонения '''
# print("df1['A'].std()")
# print(df1['A'].std())

''' Получение ковариации '''
print("df1.A.cov(df1.C)")
print(df1.A.cov(df1.C))

''' Получение коэффициента корреляции '''
print("df1.A.corr(df1.C)")
print(df1.A.corr(df1.C))