import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.graph:
            self.graph[from_vertex] = {}
        self.graph[from_vertex][to_vertex] = weight

    def dijkstra(self, start):

        distances = {vertex: float('infinity') for vertex in self.graph}

        distances[start] = 0

        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'A', 1)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'A', 4)
    graph.add_edge('C', 'B', 2)
    graph.add_edge('C', 'D', 1)
    graph.add_edge('D', 'B', 5)
    graph.add_edge('D', 'C', 1)

    start_vertex = "A"
    shortest_paths = graph.dijkstra(start_vertex)

    for vertex, distance in shortest_paths.items():
        print(f"Відстань від вершини {start_vertex} до вершини {vertex}: {distance}")
