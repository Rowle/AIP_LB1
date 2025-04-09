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
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False

def kruskal_mst(edges, num_vertices):
    edges.sort(key=lambda x: x[2])  # Сортировка по весу
    uf = UnionFind(num_vertices)
    mst = []

    for u, v, weight in edges:
        if uf.union(u - 1, v - 1):  # Преобразуем вершины к 0-индексации
            mst.append((u, v, weight))
            if len(mst) == num_vertices - 1:
                break

    return mst

# Пример использования
if __name__ == "__main__":
    filename = "graph.txt"
    num_vertices, edges = read_graph_from_file(filename)

    print("\nМинимальное остовное дерево (Краскал):")
    mst = kruskal_mst(edges, num_vertices)
    print(mst)