import heapq
# Функция для чтения графа из файла
def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Удаляем комментарии и пустые строки
    clean_lines = [line.split('#')[0].strip() for line in lines if line.strip()]

    # Количество вершин и ребер
    num_vertices = int(clean_lines[0])
    num_edges = int(clean_lines[1])

    edges = []
    for line in clean_lines[2:]:
        parts = list(map(int, line.split()))
        u, v, weight = parts
        edges.append((u, v, weight))
    return num_vertices, edges

# Функция для создания списка смежности
def adjacency_list(num_vertices, edges):
    adj_list = [[] for _ in range(num_vertices)]
    for u, v, weight in edges:
        adj_list[u - 1].append((v - 1, weight))
        adj_list[v - 1].append((u - 1, weight))  # Для неориентированного графа
    return adj_list

# Алгоритм Дейкстры
def dijkstra(adj_list, start):
    distances = [float('inf')] * len(adj_list)
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > distances[u]:
            continue
        for v, weight in adj_list[u]:
            distance = current_dist + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(heap, (distance, v))
    return distances

# Пример использования
if __name__ == "__main__":
    filename = "graph.txt"
    num_vertices, edges = read_graph_from_file(filename)

    # Создаем список смежности
    adj_list = adjacency_list(num_vertices, edges)
    print("\nКратчайшие пути от вершины 0 (Дейкстра):")
    print(dijkstra(adj_list, 0))