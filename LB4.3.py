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


# Проверка наличия Эйлерова цикла
def is_eulerian_cycle_possible(adj_list):
    for neighbors in adj_list:
        if len(neighbors) % 2 != 0:  # Если степень вершины нечетная
            return False
    return True


# Пример использования
if __name__ == "__main__":
    filename = "graph.txt"

    # Чтение графа из файла
    num_vertices, edges = read_graph_from_file(filename)

    # Создание списка смежности
    adj_list = adjacency_list(num_vertices, edges)

    print("\nВозможен ли Эйлеров цикл?")
    print(is_eulerian_cycle_possible(adj_list))