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

# Матрица смежности
def adjacency_matrix(num_vertices, edges):
    matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for u, v, weight in edges:
        matrix[u - 1][v - 1] = weight
        matrix[v - 1][u - 1] = weight  # Для неориентированного графа
    return matrix

# Матрица инцидентности
def incidence_matrix(num_vertices, edges):
    matrix = [[0] * len(edges) for _ in range(num_vertices)]
    for idx, (u, v, _) in enumerate(edges):
        matrix[u - 1][idx] = 1
        matrix[v - 1][idx] = 1
    return matrix

# Список ребер
def edge_list(edges):
    return edges

# Список смежности
def adjacency_list(num_vertices, edges):
    adj_list = [[] for _ in range(num_vertices)]
    for u, v, weight in edges:
        adj_list[u - 1].append((v - 1, weight))
        adj_list[v - 1].append((u - 1, weight))  # Для неориентированного графа
    return adj_list

# Пример использования
if __name__ == "__main__":
    filename = "graph.txt"
    num_vertices, edges = read_graph_from_file(filename)

    print("Матрица смежности:")
    print(adjacency_matrix(num_vertices, edges))

    print("\nМатрица инцидентности:")
    print(incidence_matrix(num_vertices, edges))

    print("\nСписок ребер:")
    print(edge_list(edges))

    print("\nСписок смежности:")
    print(adjacency_list(num_vertices, edges))

