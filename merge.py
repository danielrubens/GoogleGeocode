import pandas as pd

df1 = pd.read_csv('01.csv')
df2 = pd.read_csv('02.csv')
#df1['Address3'] = df1['Address3'].astype(str)
#df1['ADDRESS'] = df1['Address2']+' '+df1['Address3']
a = df2.head()
print(a)

b = pd.merge(df1,df2,how='left', on=['ADDRESS'])
c = b.head()
print(b)

b.to_csv('Max_Geocode_Final_04.csv')
#pd.merge(df1,df2,on='ADDRESS',how='outer')
#pd.merge(df1,df2,how='left',on='ADDRESS',validate='many_to_many')
#pd.merge(df1,df2,on='ADDRESS',how='right')
#df1.merge(df2, how='left', left_on='ADDRESS', right_on='ADDRESS')

df1.to_csv('Max_Geocode_Final_03')
#total_rows['ColumnID'] = total_rows['ColumnID'].astype(str)