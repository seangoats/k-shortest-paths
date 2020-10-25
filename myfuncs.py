def read_road_graph(filename):
    
    with open(f"{filename}.txt",'r') as f:
        all_lines = f.read().splitlines()
        
    all_lines = all_lines[4:]
    
    for line in range(0,len(all_lines)):
        all_lines[line] = [int(line) for line in all_lines[line].split("\t")]
        
    return create_adj_list(all_lines)

def create_adj_list(graph):
    adj_list = {}
    
    for edge in graph:
        if edge[0] not in adj_list:
            adj_list[edge[0]] = []
        adj_list[edge[0]].append(edge[1])
        
    return adj_list

def read_hospitals(filename):
    with open(f"{filename}.txt",'r') as f:
        hospitals = [int(line) for line in f.read().splitlines()[1:]]
    
    return hospitals

from itertools import combinations,groupby
import networkx as nx
from random import random

def random_graph(n,p):
    vertices = set([v for v in range(n)])
    edges = set()

    for combination in combinations(vertices,2):
        r = random()
        if r<p:
            edges.add(combination)
    
    g = nx.Graph()
    g.add_nodes_from(vertices)
    g.add_edges_from(edges)

    g = nx.to_dict_of_lists(g,vertices)
    return g
