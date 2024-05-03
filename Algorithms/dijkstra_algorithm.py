"""
Graph used for this Dijkstra's algorith implementation. 
            |A|
          *  *  \
      6  /   |   \ 1
        /    |    *  
|Start|     3|     |Finish|
        \    |    *
      2  \   |   / 5
          * |B| /
"""

""" Populate the out-neightbor hash-map """
graph = {}

# Start node and its out-neightbors
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# 'a' node out-neighbors
graph["a"] = {}
graph["a"]["finish"] = 1

# 'b' node out-neighbors
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["finish"] = 5

graph["finish"] = {} 

""" Populate the the hash-map from 'start' node """
import math 
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["finish"] = math.inf

""" Populate the the hash-map for the node parents """
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["finish"] = None  # We don't know yet whether it's node 'a' or 'b'

# Keep track of nodes already processed 
processed = set() 

def find_min_cost_node(costs: dict) -> str: 
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        # We already looked at this node 
        if node in processed:  
            continue 

        # This node is not the lowest 
        if costs[node] > lowest_cost:
            continue 
        
        # Found a new lowest cost node 
        lowest_cost = costs[node]
        lowest_cost_node = node
    
    return lowest_cost_node

def dijkstra_algorithm() -> list:
    """ This is the implementation of the Dijkstra's algorithm to 
    find the shorted weighted path from 'start' node to 'finish' node. 
    It updates the 'costs' hash-table. 

    Note: this algorithm only works for positive weighted graphs. 
    """
    current_node = find_min_cost_node(costs)
    while current_node:
        current_cost = costs[current_node]
        neighbors = graph[current_node] # Returns a hash-table 
        for node, cost in neighbors.items():
            new_cost = current_cost + cost
            # We found a shorter path to this node 
            if costs[node] > new_cost:
                costs[node] = new_cost # Update the cost with lowest value
                
                # You can get to this out-neighbor through the node currently 
                # being processed
                parents[node] = current_node 
        
        # All the out-neighbors for this node have been processed 
        processed.add(current_node) 
        current_node = find_min_cost_node(costs) # Find the next node to be processed 

if __name__ == "__main__":
    dijkstra_algorithm() 
    print(f"Shortest path from Start to Finish:")
    for to_node, from_node in parents.items():
        print(f"{from_node} -> {to_node}")
