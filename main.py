from myfuncs import *
from algos import *
import time
import random
import networkx

#test on a randomly generated node
print("Testing on a randomly generated graph: ")
test_nodes = int(input("Enter the number of nodes: "))
# test = gnp_random_connected_graph(test_nodes,0.00001)
test = nx.erdos_renyi_graph(test_nodes,1/test_nodes)
test = nx.to_dict_of_lists(test)

graph = open('graph.txt','w')
graph.write(str(test))

no_of_hospitals = int(input("Enter the number of hospitals: "))
test_hospitals = random.sample(range(0,test_nodes), no_of_hospitals)

filename = input("Enter the output file name for shortest path: ")
BFS(test,test_hospitals,filename)

k = int(input(f"Enter the k value: "))
filename = input("Enter the output file name for k shortest paths: ")
BFS2(test,test_hospitals,k,filename)

##test on sample of 10 graphs
# test = {0:[1,2],1:[0,7,8],2:[0,7,3],3:[2,5,6],4:[],5:[3,8],6:[3],7:[1,2],8:[1,5],9:[10],10:[9]}
# BFS(test,[3,5,6],'test')
# BFS2(test,[3,5,6],2,'test2')



#test on a road network
test_on_road = input("Test on a road network? [Y/n] ")

if(test_on_road.lower() == "y"):

    filename = input("Enter the road network filename: ")
    adj_list = read_road_graph(filename)

    filename = input("Enter the hospital filename: ")
    hospitals = read_hospitals(filename)


    filename = input("Enter the output file name for shortest path: ")
    BFS(adj_list,hospitals,filename)

    k = int(input("Enter the k value: "))
    filename = input("Enter the output file name for k shortest paths: ")
    BFS2(adj_list,hospitals,k,filename)
else:
    print("Ending...")



