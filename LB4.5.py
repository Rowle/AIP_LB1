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
def floyd_warshall(num_vertices, edges):
    INF = float('inf')
    dist = [[INF] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        dist[i][i] = 0
    for u, v, weight in edges:
        dist[u - 1][v - 1] = weight
        dist[v - 1][u - 1] = weight  # Для неориентированного графа

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Пример использования
if __name__ == "__main__":
    filename = "graph.txt"
    num_vertices, edges = read_graph_from_file(filename)
    print("\nМатрица кратчайших путей (Флойд):")
    print(floyd_warshall(num_vertices, edges))