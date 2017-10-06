import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()

G=nx.read_edgelist('sub_network.txt', delimiter='\t', create_using=nx.DiGraph())
nx.draw(G, arrows=True ,with_labels=True)
fig.savefig('Network-graph')

H=max(nx.strongly_connected_component_subgraphs(G), key=len)
nx.draw(H, arrows=True ,with_labels=True)
fig.savefig('SCC_max_subgraph')

#--------------------------------------------------------------------
def plot_outvsIn(G):
	InCount = = np.unique(G.in_degree().values() )         #in-degree distribution
	OutCount = = np.unique(G.out_degree().values() )     #out-degree distribution
	plt.plot(InCount, OutCount, 'o')          
	plt.xlabel('In-degree')
	plt.ylabel('Out-degree')
	plt.title('In-degree vs Out-degree in the Twitter Network')	
	fig.savefig('In-degree vs Out-degree.png')


def plot_deg_distribution(G):
	unique, counts = np.unique(G.degree().values(), return_counts=True)
	plt.plot(unique,counts, 'o')
	#plt.loglog(unique,counts)
	plt.xlabel('Degrees')
	plt.ylabel('Number of nodes')
	plt.title('Degree distribution of nodes')	
	fig.savefig('Degree distribution of nodes.png')

def plot_nodeVSin(G):
	In, nnodes = np.unique(G.in_degree().values(), return_counts=True)
	plt.plot(In,nnodes, 'o')
	plt.xlabel('In-Degrees of nodes')
	plt.ylabel('Number of nodes')	
	fig.savefig('In-Degree distribution of nodes.png')


def plot_nodeVSout(G):
	out, nnodes = np.unique(G.out_degree().values(), return_counts=True)
	plt.plot(out,nnodes, 'o')
	plt.xlabel('Out-Degrees of nodes')
	plt.ylabel('Number of nodes')	
	fig.savefig('Out-Degree distribution of nodes

#--------------------------------------------
plot_outvsIn(G)
plot_deg_distribution(G)
plot_nodeVSin(G)
plot_nodeVSout(G)
  
print nx.info(G)
print "Graph Diameter is", nx.diameter(G)
print "Graph Density is", nx.density(G)




