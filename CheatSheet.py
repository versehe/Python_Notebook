aa= list()
aa.append('value_a') 
aa.sort(reverse = True)

x=dict()
x['a'] = 1 
x.get('a','b') if can't find a, use b

store1 = [1,5,6]
store2 = [2,2,4]
cheapest = map(min, store1, store2)

if x==6:
    print ('whatever')
elif x > 5:
    print ('still whatever')
else:
    print ('see this')
	
def addtwo(a,b,c = None): # c could be none
	return a+ b 
	
while n> 0:
    print (n)
    n= n-1

yy = list()
for x in range(len(yy)):
	if x< 2:
        continue 	
		
import pandas as pd
import numpy as np
np.isNan(df)
sub_df.dropna()	
df.iat[0,2] = 'China'  #replace a value
df['Location'].value_counts()
df['store'] = df.index
df =df.set_index('Item Purchased')
df =df.reset_index()
df.describe()
df.sort_values(by=['Member_ID','Year_Start'])

df.loc[:,['Name','Cost']]
df.where(df['Cost'] > 10)
df.loc[df['Cost']>10 & (df['Item Purchased'] == 'Kitty Litter') | df['Cost'].isin([2.5,5.0]),['Cost','Item Purchased']]
df.drop('Store 1') #row
del df['Name'] #drop a column
df['cumsum'] = df.cumsum() #cumulative sum 
df['index'] = np.arange(3)

df = pd.merge(Student,Class, left_on = 'class',right_on = 'classes', how = 'inner')
# can merge on multiple keys on = ['class','Name']
df['prev_score'] = df.groupby('class',as_index=False)['Score'].shift(1)
df['rank']= df.groupby('class')['Score'].rank(ascending=False)
df.groupby(['class','Classroom']).mean()

df_name = pd.get_dummies(df['Name'])


df = pd.read_csv('zzz.txt', header = 0, skiprows = 1)
df = pd.read_excel('C:\\ddd\\file.xlsx',sheet_name='sheet1')
df= df.to_csv('foo.csv')
