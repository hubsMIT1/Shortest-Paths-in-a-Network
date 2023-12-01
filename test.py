# test.py
from files.graph import Graph

def run_tests():
    graph = Graph()

    # Test adding edges to the graph
    graph.add_edge("Belk", "Grigg", 1.2)
    graph.add_edge("Belk", "Health", 0.5)
    graph.add_edge("Duke", "Belk", 0.6)
    graph.add_edge("Belk", "Woodward", 0.25)
    graph.add_edge("Woodward", "Grigg", 1.1)
    graph.add_edge("Grigg", "Duke", 1.6)
    graph.add_edge("Health", "Woodward", 0.7)
    graph.add_edge("Health", "Education", 0.45)
    graph.add_edge("Woodward", "Education", 1.3)
    graph.add_edge("Duke", "Education", 0.3)
    graph.add_edge("Woodward", "Duke", 0.67)

    # Test printing the graph
    print("Graph after adding edges:")
    graph.print_graph()

    # Test finding shortest path
    path, total_time = graph.find_shortest_path("Belk", "Education")
    print("\nShortest Path from Belk to Education:", " -> ".join(path), "Total Time:", total_time)

    # Test marking an edge as down and finding shortest path again
    graph.edge_down("Belk", "Woodward")
    path, total_time = graph.find_shortest_path("Belk", "Education")
    print("\nShortest Path from Belk to Education after marking Belk->Woodward down:", " -> ".join(path), "Total Time:", total_time)

    # Test marking a vertex as down and finding shortest path again
    graph.vertex_down("Grigg")
    path, total_time = graph.find_shortest_path("Belk", "Education")
    print("\nShortest Path from Belk to Education after marking vertex Grigg down:", " -> ".join(path), "Total Time:", total_time)

    # Test marking an edge as up again
    graph.edge_up("Belk", "Woodward")

    # Test marking a vertex as up again
    graph.vertex_up("Grigg")

    # Test printing the updated graph
    print("\nGraph after updating edges:")
    graph.print_graph()

    # Test finding reachable vertices
    reachable_sets = graph.find_reachable_vertices()
    print("\nReachable Vertices:")
    for vertex, reachable_vertices in reachable_sets.items():
        print(f"{vertex}: {', '.join(reachable_vertices)}")

if __name__ == "__main__":
    run_tests()
