import pandas as pd
import sys
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np

#inputs------------------------------------------
topic_composition = sys.argv[1]
allusers= sys.argv[2]     
usermap_june= sys.argv[3]
twitter_net= sys.argv[4]
#outputs
usrname= sys.argv[5]
user_id= sys.argv[6]
subnetwork_output= sys.argv[7]
wcc_plot= sys.argv[8]
scc_plot= sys.argv[9]
diametervsnodes= sys.argv[10]
#--------------------------get usernames and user id---------

d= pd.read_csv(topic_composition, header=None, sep="\t")
df = pd.read_csv(allusers, header=None, sep="\t")   
df.columns=["users"]             
df['Max'] = d.idxmax(axis=1)
d1= pd.read_csv(usermap_june, sep="\t" ,header=None)
d1.columns=['user','id']
d2=pd.read_csv(twitter_net, sep="\t" ,header=None)
d2.columns=['A','B']

#print("Loading Done...")

username=[]
userid=[]
G_size=[]
scc_size=[]
wcc_size=[]
dia=[]
avg_in=[]
avg_out=[]
avg_deg=[]

#print("Starting Diameter calculation...")

for i in range(len(d.columns)):
	print(topic_composition+" "+str(i))
	un= df.loc[df['Max']== i, ['users']]
	un=un[~un.duplicated()]
	username.append(un)
	l=un.users.tolist()
	l=list(set(l))
	uid=d1[d1['user'].isin(l)]
	userid.append(uid)
	l1=uid['id'].tolist()
	netwrk= d2[d2.A.isin(l1)]
	netwrk= netwrk[netwrk.B.isin(l1)]
	G=nx.from_pandas_dataframe(netwrk,'B','A', create_using=nx.DiGraph())	
	G_size.append(len(G))
	sc=max(nx.strongly_connected_component_subgraphs(G), key=len)
	scc_size.append(len(sc))	
	wc=max(nx.weakly_connected_component_subgraphs(G), key=len)
	wcc_size.append(len(wc))
	try:
		diamet=nx.diameter(sc)
	except:
		diamet="nan"                         
	dia.append(diamet)	
	avg_in.append(sum(G.in_degree().values())/float(len(G)))
	avg_out.append(sum(G.out_degree().values())/float(len(G)))
	avg_deg.append(sum(G.degree().values())/float(len(G)))
	#print("done")

df1=pd.concat(username, axis=1)  
df2=pd.concat(userid, axis=1)
df3 = pd.DataFrame({'Nodes': G_size, 'SCC': scc_size, 'WCC': wcc_size, 'diameter': dia, 'avg-degree': avg_deg, 'avg-out-degree': avg_out, 'avg-in-degree': avg_in})


df1.to_csv(usrname, sep='\t')
df2.to_csv(user_id, sep='\t')
df3.to_csv(subnetwork_output, sep='\t')

#PLOT(10 plots:1 plot for each numtopic)__________________________________________________________________________________

def plot_wcc():
	plt.plot(wcc_size, G_size,'o')
	plt.xlabel('Size of Largest WCC', fontsize=25)
        plt.ylabel('Cluster Size (No. of Nodes)', fontsize=25)
	plt.xticks(fontsize=18)
	plt.yticks(fontsize=18)
	plt.tight_layout()
	plt.savefig(wcc_plot +'.png')
	plt.clf()

def plot_scc():
	plt.plot(scc_size, G_size, 'o')
	plt.xlabel('Size of Largest SCC', fontsize=25)
        plt.ylabel('Cluster Size (No. of Nodes)', fontsize=25)
	plt.xticks(fontsize=18)
	plt.yticks(fontsize=18)
	plt.tight_layout()
	plt.savefig(scc_plot +'.png')
	plt.clf()

def plot_diameter():
	plt.plot(dia, G_size, 'o')
	plt.xlabel('Diameter of A Largest SCC', fontsize=25)
	plt.ylabel('Cluster Size (No. of Nodes)', fontsize=25)
	plt.xticks(fontsize=18)
	plt.yticks(fontsize=18)
	plt.tight_layout()
	plt.savefig(diametervsnodes +'.png')
	plt.clf()	

plot_wcc()
plot_scc()
plot_diameter()
