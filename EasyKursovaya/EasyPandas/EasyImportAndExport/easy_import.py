import pandas as pd

'''
Импорт данных из сторонних источников
'''

''' Импорт данных из csv '''
# df = pd.read_csv('test_file.csv')
''' Импорт данных из json '''
# df = pd.read_json('https://www.fedstat.ru/indicator/dataGrid.do?id=30957')
''' Импорт данных из csv '''
# df = pd.read_table('test_file.csv',sep=',')
''' Импорт данных из excel '''
# df = pd.read_excel('trade_stats.xlsx')
''' Импорт данных из html '''
# df = pd.read_html('https://www.championat.com/olympicwinter/_sochiog/tournament/647/standing/', attrs={'class': 'medals-table'})
''' Импорт данных из xml '''
df = pd.read_xml('../temp/cb_data.xml')

print(df)


