from myfuncs import *
from algos import *
import time
import random

#test on a randomly generated node
print("Testing on a randomly generated graph: ")
test_nodes = int(input("Enter the number of nodes: "))
test = gnp_random_connected_graph(test_nodes,0.00001)
test = nx.to_dict_of_lists(test)
no_of_hospitals = int(input("Enter the number of hospitals: "))
test_hospitals = random.sample(range(0,test_nodes), no_of_hospitals)
BFS(test,test_hospitals,input("Enter the output file name for shortest path: "))
BFS2(test,test_hospitals,int(input(f"Enter the k value: ")),input("Enter the output file name for k shortest paths: "))


#test on a road network
test_on_road = input("Test on a road network? [Y/n]")
if(test_on_road.lower() == "y"):
    adj_list = read_road_graph(input("Enter the road network filename: "))

    hospitals = read_hospitals(input("Enter the hospital filename: "))



    BFS(adj_list,hospitals,input("Enter the output file name for shortest path: "))


    BFS2(adj_list,hospitals,int(input("Enter the k value: ")),input("Enter the output file name for k shortest paths: "))
else:
    print("Ending...")



