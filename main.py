from myfuncs import *
from algos import *
import time
import random
import networkx


#test on a randomly generated node
while True:
    try:
        choice = int(input("Enter a choice:\n1:Random Graph\n2:Small test graph with 10 nodes\n3:Road Network\nTo exit, enter any other number:   "))

        if choice == 1:
            print("Testing on a randomly generated graph: ")
            test_nodes = int(input("Enter the number of nodes: "))
            test = gnp_random_connected_graph(test_nodes,0.00001)
            test = nx.to_dict_of_lists(test)

            no_of_hospitals = int(input("Enter the number of hospitals: "))
            test_hospitals = random.sample(range(0,test_nodes), no_of_hospitals)

            print("Starting BFS shortest path algorithm...")
            filename = input("Enter the output file name for shortest path: ")
            BFS(test,test_hospitals,filename)
            
            print("Starting BFS k shortest paths algorithm")
            k = int(input(f"Enter the k value: "))
            filename = input("Enter the output file name for k shortest paths: ")
            BFS2(test,test_hospitals,k,filename)

        elif choice == 2:
            ##test on sample of 10 graphs
            print("Testing on sample graph with 10 nodes: ")
            test = {0:[1,2],1:[0,7,8],2:[0,7,3],3:[2,5,6],4:[],5:[3,8],6:[3],7:[1,2],8:[1,5],9:[10],10:[9]}
            test = {1:[2,6],2:[1,3,6],3:[2,4,5,6],4:[3,5],5:[3,4,6],6:[1,2,3,5]}
            print("Starting BFS shortest path algorithm")
            BFS(test,[1,5],'test')
            print("Starting BFS k shortest paths algorithm")
            BFS2(test,[3,5,6],2,'test2')



    #test on a road network
        elif choice == 3:
            filename = input("Enter the road network filename: ")
            adj_list = read_road_graph(filename)

            filename = input("Enter the hospital filename: ")
            hospitals = read_hospitals(filename)

            print("Starting BFS shortest path algorithm")
            filename = input("Enter the output file name for shortest path: ")
            BFS(adj_list,hospitals,filename)

            print("Starting BFS k shortest paths algorithm")
            k = int(input("Enter the k value: "))
            filename = input("Enter the output file name for k shortest paths: ")
            BFS2(adj_list,hospitals,k,filename)
        else:
            print("Exiting program...")
            break
    except:
        print("Invalid input, please try again!")





