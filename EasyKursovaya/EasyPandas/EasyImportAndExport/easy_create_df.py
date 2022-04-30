import pandas as pd

'''
Создание объекта Dataframe
'''

df = pd.DataFrame([['John', 'Wick', 'male', 50],
                  ['Sasha', 'White', 'female', 32],
                  ['Egor', 'Letov', 'male', 43]],
                  index=['zero', 'one', 'two'],
                  columns=['name', 'surname', 'sex', 'age'])

print(df)



