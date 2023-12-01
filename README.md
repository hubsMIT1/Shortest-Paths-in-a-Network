# Network Routing Project

## Files

### `edge.py`

This file defines the `Edge` class, which represents a directed edge in the network graph. Each edge has a tail vertex, a head vertex, a transmission time, and a flag indicating whether the edge is currently available (`is_up`).

### `vertex.py`

This file defines the `Vertex` class, representing a vertex in the network graph. Each vertex contains a list of outgoing edges (`edges`), and a flag indicating whether the vertex is currently available (`is_up`).

### `graph.py`

The `Graph` class is defined in this file, representing the entire network graph. It includes methods for adding vertices and edges, updating edge and vertex states, finding the shortest path using Dijkstra's algorithm, printing the graph, and identifying reachable vertices.

### `main.py`

This file serves as an example of how to interact with the `Graph` class. It reads input queries from the standard input and executes corresponding actions such as adding edges, deleting edges, finding the shortest path, and printing the graph.

### `test.py`

This file contains a set of test cases to validate the functionality of the `Graph` class. Run this script (e.g., `python test.py`) to check if the implemented methods work correctly.

## Usage

1. **Testing the Implementation:**

   Run the test script to validate the correctness of the implemented functionalities:

   ```bash
   python test.py

2. **Running the Main Program:**

   Execute the main script to interact with the graph and perform various actions:

   ```bash
   python main.py network.txt
    > add Belk Grigg 1.2 
    > path Belk Grigg
    

    and so on...
