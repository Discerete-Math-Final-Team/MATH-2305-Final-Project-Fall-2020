'''
import networkx as nx
from functions import * 
from drawing import *
from algorithms import *
'''
import networkx as nx
from functions import * 
from drawing import *
from algorithms import *

'''
will open and return a file object from test-graphs folder in this case a graph to be read,
if file is not found will raise an error
NetworkX will then generate a plot for the chosen file
It will then ask for an input for a starting vertex and will
ensure returning a hashable type
'''
graph_data = open('test-graphs/G4.txt','r') #read in the graph you want to test G1-G4

G = nx.read_weighted_edgelist(graph_data, nodetype = int) #create initial graph 

T = prims_algorithm(G, int(input("Type starting vertex: ")), True, True) #ask the user what verticy they want to start on
