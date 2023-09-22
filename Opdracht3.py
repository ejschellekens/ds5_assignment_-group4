# Excersice 3.1
import networkx as nx
import matplotlib.pyplot as plt
import random as random
import csv

def drawNetwork(N, M):
    G = nx.Graph()
    G.add_nodes_from(range(1, N + 1))

    # Create a list of nodes to connect to
    nodes_to_connect = list(G.nodes)

    # Loop through the nodes and add edges to make each node 4-regular
    for node in G.nodes:
        # Shuffle the list of nodes to connect to
        random.shuffle(nodes_to_connect)

        # Remove the current node from the list to prevent self-connection
        nodes_to_connect.remove(node)
        
        # Connect the node to the first 4 nodes in the shuffled list
        for neighbor in nodes_to_connect[:M]:
            G.add_edge(node, neighbor)

    pr = nx.pagerank(G)
    
    lists = sorted(pr.items()) # sorted by key, return a list of tuples

    x, y = zip(*lists) # unpack a list of pairs into two tuples

    plt.plot(x, y)
    plt.show()
    #nx.draw(G, node_color = 'green',node_size = 100) #For drawing notes

def drawSquirrelNetwork():
    dict_data = {}

    with open('squirrel_edges.csv', mode='r', newline='') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Skip the header row (if it exists)
        next(csv_reader, None)
        
        # Iterate through the rows and add them to the dictionary
        for row in csv_reader:
            # Assuming the first column is the key and the second is the value
            key, value = row[0], row[1]
            dict_data[key] = value

    G = nx.DiGraph(dict_data)
    pr = nx.pagerank(G)
    lists = sorted(pr.items()) # sorted by key, return a list of tuples

    x, y = zip(*lists) # unpack a list of pairs into two tuples

    plt.plot(x, y)
    plt.show()

drawNetwork(400, 4)
drawSquirrelNetwork()    