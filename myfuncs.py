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
import random

def gnp_random_connected_graph(n, p):
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted

    n: int -> number of nodes
    0<p<1: probability of edges between nodes
    """
    edges = combinations(range(n), 2)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < p:
                G.add_edge(*e)
    return G
