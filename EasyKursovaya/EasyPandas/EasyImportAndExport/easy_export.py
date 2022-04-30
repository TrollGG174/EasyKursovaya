import pandas as pd

'''
Экспорт данных
'''

df = pd.read_xml('../temp/cb_data.xml')

f = open('../temp/example.html', 'w')
f.write(df.to_html())
f.close()

''' Экспорт данных в html '''
# print(df.to_html())
''' Экспорт данных в json '''
# print(df.to_json())
''' Экспорт данных в csv '''
# print(df.to_csv())
''' Экспорт данных в xml '''
# print(df.to_xml())
''' Экспорт данных в excel '''
# print(df.to_excel())
''' Экспорт данных в sql'''
# print(df.to_sql())
''' Экспорт данных в строку '''
# print(df.to_string())

