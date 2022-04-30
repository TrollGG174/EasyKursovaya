import pandas as pd

'''
Работа с основными функциями
'''

df = pd.read_xml('../temp/cb_data.xml')

''' Получение первых 6 строк Dataframe '''
# print(df.head(6))
''' Получение последних 6 строк Dataframe '''
# print(df.tail(6))
''' Получение отдельного столбца '''
# print(df.Name)
# print(df['Name'])
''' Получение типа данных '''
# print(type(df.Name))

''' Пример работы с несколькими столбцами '''
s = df[['Name', 'NumCode', 'Value']]

def convert_currency(val):
    new_val = val.replace(',', '.')
    return float(new_val)

new_df = s.rename(columns={'NumCode': 'Count'})
new_df['Value'] = new_df['Value'].apply(convert_currency)
new_df['Cnt_Val'] = new_df['Count'] * new_df['Value']

''' Фильтрациях числовых данных '''
df_with_num_condition = new_df[new_df.Cnt_Val < 10000]
# print(df_with_num_condition)

''' Фильтрациях строковых данных '''
df_with_str_condition = new_df[new_df.Name.str.contains('доллар')]
# print(df_with_str_condition)

''' Фильтрациях с несколькими условиями '''
# df_with_conditions = new_df[~(new_df.Name.str.contains('доллар')) | (new_df.Cnt_Val < 10000)]
df_with_conditions = new_df[~(new_df.Name.str.contains('доллар')) & (new_df.Cnt_Val < 10000)]
# print(df_with_conditions)

''' Пример работы с loc и iloc '''
let_df = new_df.rename(index=lambda x: chr(x+97))

loc_example = let_df.loc[['d', 'm'], ['Name', 'Value']]

iloc_example = let_df.iloc[[3, 12], [0, 2]]

''' Примеры объединения данных '''
part1 = new_df.iloc[0:5]
part2 = new_df.iloc[10:15]

concat_example = pd.concat([part1, part2])

concat_example = concat_example.reset_index(drop=True)

# print(concat_example)

left_part = new_df.iloc[0:12, [0, 1, 2]]
right_part = new_df.iloc[0:12, [2, 3]]

merge_example = pd.merge(left_part, right_part)

# print(merge_example)
