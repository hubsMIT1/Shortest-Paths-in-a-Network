from files.graph import Graph
import sys

def read_graph_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]
    
def main():
    
    
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Read graph information from the file
    graph_info = read_graph_from_file(input_file)

    # Create a graph and add edges from the file
    graph = Graph()
    for line in graph_info:
        parts = line.split()
        tail, head, transmit_time = parts[0], parts[1], float(parts[2])
        graph.add_edge(tail, head, transmit_time)

    while True:
        query = input("Enter a query (add, delete, edgeup, edgedown, vertexup, vertexdown, path, print, reachable, quit): ")
        if query == 'quit':
            break
        execute_query(graph, query)
    

def execute_query(graph, query):
    
    parts = query.split()

    if parts[0] == 'add':
        graph.add_edge(parts[1], parts[2], float(parts[3]))
    elif parts[0] == 'delete':
        graph.delete_edge(parts[1], parts[2])
    elif parts[0] == 'edgeup':
        graph.edge_up(parts[1], parts[2])
    elif parts[0] == 'edgedown':
        graph.edge_down(parts[1], parts[2])
    elif parts[0] == 'vertexup':
        graph.vertex_up(parts[1])
    elif parts[0] == 'vertexdown':
        graph.vertex_down(parts[1])
    elif parts[0] == 'path':
        path, total_time = graph.find_shortest_path(parts[1], parts[2])
        print("Shortest Path:", " -> ".join(path), "Total Time:", total_time)
    elif parts[0] == 'print':
        graph.print_graph()
    elif parts[0] == 'reachable':
        reachable_sets = graph.find_reachable_vertices()
        for vertex, reachable_vertices in reachable_sets.items():
            print(f"{vertex}: {', '.join(reachable_vertices)}")
    else:
        print("Invalid query. Please enter a valid query.")

if __name__ == "__main__":
    main()
