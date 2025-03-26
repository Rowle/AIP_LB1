from queue import Queue
import random

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

 #2 Вычисление количества узлов бинарного дерева#
    def count_nodes(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.l) + self._count_nodes(node.r)

 #3 Вычисление количества листьев бинарного дерева#
    def count_leaves(self):
        return self._count_leaves(self.root)

    def _count_leaves(self, node):
        if node is None:
            return 0
        if node.l is None and node.r is None:
            return 1
        return self._count_leaves(node.l) + self._count_leaves(node.r)

#4 Вычисление высоты бинарного дерева#
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.l), self._height(node.r))

#5 Обход в глубину с использованием стека#
    def DFS_stack(self):
        if self.root is None:
            print("Дерево не существует")
            return

        stack = [self.root]
        while stack:
            node = stack.pop()
            print(str(node.v), end=' ')
            if node.r is not None:
                stack.append(node.r)
            if node.l is not None:
                stack.append(node.l)
        print()

#6 Красивый вывод бинарного дерева#
    def pretty_print(self):
        if self.root is None:
            print("Дерево не существует")
            return

        levels = []
        q = Queue()
        q.put(self.root)

        while not q.empty():
            level_size = q.qsize()
            current_level = []

            for _ in range(level_size):
                node = q.get()
                current_level.append(str(node.v))
                if node.l is not None:
                    q.put(node.l)
                if node.r is not None:
                    q.put(node.r)

            levels.append(current_level)

        max_width = 2 ** (len(levels) - 1) * 3
        for i, level in enumerate(levels):
            spacing = ' ' * (max_width // (2 ** i))
            print(spacing.join(level))


# Пример использования
if __name__ == "__main__":
    n = 10
    start = 1
    end = 100

    random_numbers = random.sample(range(start, end + 1), n)
    print(f"Сгенерированные числа: {random_numbers}")

    bst = Tree()
    for num in random_numbers:
        bst.add(num)

    print("Количество узлов:", bst.count_nodes())
    print("Количество листьев:", bst.count_leaves())
    print("Высота дерева:", bst.height())

    print("\nОбход в глубину (стек):")
    bst.DFS_stack()

    print("\nКрасивый вывод дерева:")
    bst.pretty_print()