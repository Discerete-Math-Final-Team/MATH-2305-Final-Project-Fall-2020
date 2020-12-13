import networkx as nx
from functions import *
from algorithms import prims_algorithm
from drawing import *
'''
will open and return a file object from test-graphs folder in this case a graph to be read,
if file is not found will raise an error
NetworkX will then generate a plot for the chosen file
It will then ask for an input for a starting vertex and will
ensure returning a hashable type
'''
graph_data = open('test-graphs/G1.txt', 'r')

G=nx.read_weighted_edgelist(graph_data, nodetype=int)

T= prims_algorithm(G, 0, show_graph = True, show_cost = True)

