import numpy as np
import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],}
exam_data['labels']=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df=pd.DataFrame(exam_data)
print(df)
df=df.set_index('labels')
#print 3 first rows
print(df.head(3))
#drop rows withnan values
df=df.dropna()
print(df)
#extract name and score columns
d3 = df.iloc[:, 0:2]
print(d3)
d2={'name' :["Suresh"],'score': [15.5],'attempts': [1],'qualify': ['yes']}
k=pd.DataFrame(d2)
df=pd.concat([df,k])
print(df)
df=df
df=df.drop("attempts",axis=1)
print(df)
#create new dict for success
d1={'Success':[]}

for i in df.itertuples():
    if i[2]>=10:
        d1['Success'].append(1)
    else:
         d1['Success'].append(0)

#adding the new column of success in the dataframe
df['success']=d1['Success']
print(df)
#exportingit into csv file
df.to_csv("my_data")