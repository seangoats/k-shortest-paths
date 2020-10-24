import collections

#can use random generated adjlist as graph input
def BFS(graph,hospitals,filename):
    """
    graph: adj_list format (dict of lists) of the graph to search on\n
    hospitals: list containing the hospitals\n
    filename: string containing the desired filename\n
    """
    
    print("Starting BFS shortest path algortihm")
    #Create the queue, visited set and a dictionary to store distances, initialized to 0
    queue = collections.deque()
    visited = set()
    path = {key:0 for key in graph.keys()}
    
    #Add the hospitals to queue, implication is we start exploring from hospital nodes as source
    for node in hospitals:
        visited.add(node)
        queue.appendleft(node)
        

    while queue:
        vertex = queue.pop()
        
        for neighbour in graph[vertex]:
            
            if neighbour not in visited:
                queue.appendleft(neighbour)
                path[neighbour] = path[vertex]+1
                visited.add(neighbour)
                
    #Writing the distance to an output file
    output = open(f"{filename}.txt","w")
    output.write("Node : Shortest path to a hospital\n")
    for node,shortest_path in path.items():
        if node not in visited:
            shortest_path = ["#"]
        output.write(f"{node} : {shortest_path}\n")
    print(f"Output can be found in {filename}.txt")
    print("Ending...\n")



#can use random generated adjlist as graph input
def BFS2(graph,hospitals,k,filename):

    """
    graph: adj_list format (dict of lists) of the graph to search on
    hospitals: list containing the hospitals
    k: The top-k hospitals to search
    filename: string containing the desired filename

    """
    print("Starting k shortest paths BFS algortihm")
    #Create the queue, visited set and a dictionary to store distances, initialized to 0
    queue = collections.deque()
    visited = set()
    path = {key:[0 for i in range(len(hospitals))] for key in graph.keys()}
        
    for i in range(len(hospitals)):
        visited.add(hospitals[i])
        queue.appendleft(hospitals[i])
        while queue:
            vertex = queue.pop()

            for neighbour in graph[vertex]:

                if neighbour not in visited:
                    queue.appendleft(neighbour)
                    path[neighbour][i] = path[vertex][i]+1
                    visited.add(neighbour)
        visited = set()
                
    #Writing the distance to an output file
    output = open(f"{filename}.txt","w")
    output.write(f"Node : Top {k} Shortest paths to hospitals\n")
    for node,shortest_path in path.items():
        if shortest_path[1] == shortest_path[0] == 0:
            shortest_path = ["#"]
        output.write(f"{node} : {sorted(shortest_path)[0:k]}\n")
    print(f"Output can be found in {filename}.txt")
    print("Ending...\n")
                