import heapq

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def get_ways(self): 
        """
        Чтение графа из файла и возвращение списка ребер.
        """
        index = -1

        with open(self.graph, 'r') as f:
            lines = f.readlines()
            
            for i, line in enumerate(lines):
                if '<Edges>' in line:
                    index = i
                    break

            if index != -1:
                graph = lines[index + 1:]
                return graph
            else:
                return []          

    def get_graph(self, ways):
        """
        Построение графа в виде словаря из списка ребер.
        """
        graph = dict()  
        
        for i in ways:
            a, b, weight = i.split()[0], i.split()[1], i.split()[2].strip('""')
            
            if weight == '':
                continue

            if a not in graph:
                graph[a] = dict()
                
            if b not in graph:
                graph[b] = dict()
            
            graph[a][b] = int(weight)
            graph[b][a] = int(weight)

        return dict(sorted(graph.items()))
    
    def dijkstra(self, graph, start):
        """
        Реализация алгоритма Дейкстры для поиска кратчайших путей.
        """
        if start not in graph:
            raise ValueError('Начальная вершина не найдена в графе')
        
        distances = {vertex: float('infinity') for vertex in graph}
        previous_vertices = {vertex: None for vertex in graph}
        distances[start] = 0

        priority_queue = [(0, start)]
        
        while priority_queue:   
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex   
                    heapq.heappush(priority_queue, (distance, neighbor))    

        return self.build_paths(previous_vertices, start)
    
    def build_paths(self, previous_vertices, start):
        """
        Построение путей из результата алгоритма Дейкстры.
        """
        paths = {}
        
        for vertex in previous_vertices:
            if vertex == start:
                continue

            path = []
            current_vertex = vertex

            while current_vertex is not None:
                path.insert(0, current_vertex)
                current_vertex = previous_vertices[current_vertex]

            paths[vertex] = path

        return paths.values()

    def get_tree(self, paths, graph, ways):
        """
        Формирование списка ребер с обновленными цветами.
        """
        res = []
        tree = []

        # Формируем список res из путей и графа
        for path in paths:
            for j in range(len(path) - 1):
                line = ' '.join((path[j], path[j+1], f'"{graph[path[j]][path[j+1]]}"', 'rgb(0,0,0)\n'))
                if line not in res:
                    res.append(line)

        # Создаем словарь цветов
        colors = {}
        for i in ways:
            a, b, weight, color = i.split()
            colors[(a, b, weight)] = color 
        
        for i in ways:
            a, b, weight, color = i.split()
            key = (a, b, weight)
            line = ' '.join((a, b, weight, f'{colors[key]}\n'))
            reversed_line = ' '.join((b, a, weight, f'{colors[key]}\n'))

            if line in res or reversed_line in res:
                colors[key] = 'rgb(255,0,0)'
            
            tree.append(' '.join((a, b, weight, f'{colors[key]}\n')))

        return tree


    def create_input_file(self, tree): 
        """
        Создание выходного файла с обновленными ребрами.
        """
        with open(self.graph, 'r') as input_file:
            copy = []
            lines = input_file.readlines()
            for i in lines:
                if i.strip() == '<Edges>':
                    break
                copy.append(i)
        
        with open('input.txt', 'w') as output_file:
            for line in copy:
                output_file.write(line)
            
            output_file.write('<Edges>' + '\n')

            for line in tree:
                 output_file.write(line)


graph_file = 'graph_data.txt'
graph_processor = Graph(graph_file)
ways = graph_processor.get_ways()
graph = graph_processor.get_graph(ways)
start = input("Введите начальную вершину: ")
paths = graph_processor.dijkstra(graph, start)
tree = graph_processor.get_tree(paths, graph, ways)
graph_processor.create_input_file(tree)