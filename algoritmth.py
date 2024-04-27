import sys 


class Graph:
    def __init__(self, graph, src):
        self.graph = graph
        self.src = src 


    def find_min_dist(self, dist, sptSet, count_vertices):
        min_val = sys.maxsize
        min_ind = -1

        for v in range(count_vertices):
            if dist[v] < min_val and not sptSet[v]:
                min_val = dist[v]
                min_ind = v

        return min_ind
    
    def print_path(self, parent, j):
        if parent[j] == -1:
            print(j, end=" ")
            return
        self.print_path(parent, parent[j])
        print(j, end=" ")
    
    def print_solution(self, dist, parent, tree):
        src = self.src
        
        print(f"Vertex \t\t Distance from Source {src} \t\t Path")
        for i in range(1, len(dist)):
            print(f"\n{src} -> {i} \t\t {dist[i]}\t\t\t\t", end=" ")
            self.print_path(parent, i)
        
        print("\n\nMatrix:")
        for row in tree:
            print(row)


    def dijkstra(self):
        count_vertices = len(self.graph)

        distances = [sys.maxsize] * count_vertices
        distances[self.src] = 0

        sptSet = [False] * count_vertices
        parents = [-1] * count_vertices

        geo_tree = [[0 for _ in range(count_vertices)] for _ in range(count_vertices)]

        for _ in range(count_vertices):
            min_v = self.find_min_dist(distances, sptSet, count_vertices)
            if min_v == -1:
                break    
            sptSet[min_v] = True

            for v in range(count_vertices):
                if self.graph[min_v][v] > 0 and not sptSet[v] and distances[v] > distances[min_v] + self.graph[min_v][v]:
                    distances[v] = distances[min_v] + self.graph[min_v][v]
                    parents[v] = min_v
                    geo_tree[min_v][v] = self.graph[min_v][v]
        
        self.print_solution(distances, parents, geo_tree)
        return geo_tree  



graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

G = Graph(graph, 0).dijkstra()

