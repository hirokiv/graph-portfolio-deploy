import json 
from collections import deque

# Filter out unrelated nodes
def filter_unrelated_nodes(elements):
    # Get all node IDs that are connected by edges
    connected_node_ids = set()
    for edge in elements["edges"]:
        connected_node_ids.add(edge["data"]["source"])
        connected_node_ids.add(edge["data"]["target"])

    # Filter nodes to include only those that are connected
    filtered_nodes = [
        node for node in elements["nodes"] if node["data"]["id"] in connected_node_ids
    ]

    # Return the filtered elements
    return {"nodes": filtered_nodes, "edges": elements["edges"]}

def filter_connected_component(graph_data, start_node_id):
    """
    Filters the graph to include only the connected component containing the start_node_id.
    """
    # Step 1: Build adjacency list for the graph
    adjacency_list = {}
    for edge in graph_data["edges"]:
        source = edge["data"]["source"]
        target = edge["data"]["target"]
        if source not in adjacency_list:
            adjacency_list[source] = []
        if target not in adjacency_list:
            adjacency_list[target] = []
        adjacency_list[source].append(target)
        adjacency_list[target].append(source)

    # Step 2: Perform BFS/DFS to find all connected nodes
    connected_nodes = set()
    queue = deque([start_node_id])
    while queue:
        current_node = queue.popleft()
        if current_node not in connected_nodes:
            connected_nodes.add(current_node)
            queue.extend(adjacency_list.get(current_node, []))

    # Step 3: Filter nodes and edges based on connected nodes
    filtered_nodes = [
        node for node in graph_data["nodes"] if node["data"]["id"] in connected_nodes
    ]
    filtered_edges = [
        edge
        for edge in graph_data["edges"]
        if edge["data"]["source"] in connected_nodes and edge["data"]["target"] in connected_nodes
    ]

    # Return the filtered graph
    return {"nodes": filtered_nodes, "edges": filtered_edges}

