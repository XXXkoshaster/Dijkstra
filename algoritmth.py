import sys 


class Graph:
    def __init__(self, graph, src):
        self.graph = graph
        self.src = src 


    def find_min_dist(self, dist, sptSet, count_nodes):
        min_val = sys.maxsize
        min_ind = -1

        for v in range(count_nodes):
            if dist[v] < min_val and not sptSet[v]:
                min_val = dist[v]
                min_ind = v

        return min_ind
    
    
    def dijkstra(self):
        count_nodes = len(self.graph)

        distances = [sys.maxsize] * count_nodes
        distances[self.src] = 0

        sptSet = [False] * count_nodes

        geo_tree = [[0 for _ in range(count_nodes)] for _ in range(count_nodes)]

        for _ in range(count_nodes):
            min_v = self.find_min_dist(distances, sptSet, count_nodes)
            if min_v == -1:
                break    
            sptSet[min_v] = True

            for v in range(count_nodes):
                if self.graph[min_v][v] > 0 and not sptSet[v] and distances[v] > distances[min_v] + self.graph[min_v][v]:
                    distances[v] = distances[min_v] + self.graph[min_v][v]

                    geo_tree[min_v][v] = self.graph[min_v][v]

        return geo_tree  


graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 0, 10, 0, 2, 0, 0],
         [0, 0, 0, 14, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]

G = Graph(graph, 0)
shortest_path_tree = G.dijkstra()

for row in shortest_path_tree:
    print(row)