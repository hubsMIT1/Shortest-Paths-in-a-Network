# graph.py
import heapq
from files.edge import Edge
from files.vertex import Vertex
from decimal import Decimal

class Graph:
    def __init__(self):
        self.vertices = {}  

    def add_vertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = Vertex(name)

    def add_edge(self, tail, head, transmit_time):
        if tail not in self.vertices:
            self.add_vertex(tail)
        if head not in self.vertices:
            self.add_vertex(head)

        edge = Edge(tail, head, transmit_time)
        self.vertices[tail].edges.append(edge)
        
        reverse_edge = Edge(head, tail, transmit_time)
        self.vertices[head].edges.append(reverse_edge)

    def delete_edge(self, tail, head):
        if tail in self.vertices and head in self.vertices:
            self.vertices[tail].edges = [edge for edge in self.vertices[tail].edges if edge.head != head]

    def edge_down(self, tail, head):
        for edge in self.vertices[tail].edges:
            if edge.head == head:
                edge.is_up = False

    def edge_up(self, tail, head):
        for edge in self.vertices[tail].edges:
            if edge.head == head:
                edge.is_up = True

    def vertex_down(self, vertex_name):
        if vertex_name in self.vertices:
            self.vertices[vertex_name].is_up = False

    def vertex_up(self, vertex_name):
        if vertex_name in self.vertices:
            self.vertices[vertex_name].is_up = True

    def find_shortest_path(self, from_vertex, to_vertex):
        # Implement Dijkstra's algorithm here

        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[from_vertex] = 0
        priority_queue = [(0, from_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_vertex not in self.vertices or not self.vertices[current_vertex].is_up:
                continue

            for edge in self.vertices[current_vertex].edges:
                if not edge.is_up:
                    continue
                current_distance = Decimal(str(current_distance))
                edge_tt = Decimal(str(edge.transmit_time))
                new_distance = current_distance + edge_tt

                if new_distance < distances[edge.head]:
                    distances[edge.head] = new_distance
                    heapq.heappush(priority_queue, (new_distance, edge.head))

        path = []
        current = to_vertex
        while current != from_vertex:
            path.append(current)
            candidates = [
                edge.tail for edge in self.vertices[current].edges
                if edge.is_up and distances[edge.tail] == Decimal(str(distances[current])) - Decimal(str(edge.transmit_time))
            ]

            if candidates:
                current = min(candidates, key=lambda x: self.vertices[x].is_up)
            else:
                break
        path.append(from_vertex)
        return list(reversed(path)), distances[to_vertex]

    def print_graph(self):
        for vertex_name in sorted(self.vertices):
            print(vertex_name)
            for edge in sorted(self.vertices[vertex_name].edges, key=lambda x: x.head):
                print(f"  {edge.head}{' DOWN' if not edge.is_up else ''} {edge.transmit_time}")

    def find_reachable_vertices(self):
        reachable_sets = {}
        for vertex_name in sorted(self.vertices):
            if not self.vertices[vertex_name].is_up:
                continue

            visited = set()
            stack = [vertex_name]

            while stack:
                current_vertex = stack.pop()
                if current_vertex not in visited:
                    visited.add(current_vertex)
                    stack.extend(edge.head for edge in self.vertices[current_vertex].edges if edge.is_up)

            reachable_sets[vertex_name] = sorted(visited)

        return reachable_sets
