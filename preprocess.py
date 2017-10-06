#preprocess edgelist 

import pandas as pd

d= pd.read_csv('usermap_june', sep="\t" ,header=None)
d.columns=['user','id']

with open('users', 'r') as f:
	l=f.read().splitlines()

l=list(set(l))

df=d[d['user'].isin(l)]

#df1.to_csv('usermap',sep='\t', index=None)

dfList = df['id'].tolist()

d1=pd.read_csv('twitter_rv.net', sep="\t" ,header=None)
d1.columns=['A','B']

df1= d1[d1.A.isin(dfList)]
df1= df1[df1.B.isin(dfList)]

df1 = df1[['B', 'A']]

df1.to_csv('sub_network.txt', sep='\t', index=None, header=False)



