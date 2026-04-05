import networkx as nx

def create_graph():
    G = nx.Graph()
    
    edges = [
        (0, 1, 2),
        (1, 2, 3),
        (0, 2, 4),
        (2, 3, 1)
    ]
    
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
    
    return G


def shortest_path_solution():
    G = create_graph()
    path = nx.shortest_path(G, source=0, target=3, weight='weight')
    cost = nx.shortest_path_length(G, source=0, target=3, weight='weight')
    
    return path, cost


if __name__ == "__main__":
    path, cost = shortest_path_solution()
    print("Best Path:", path)
    print("Cost:", cost)
    