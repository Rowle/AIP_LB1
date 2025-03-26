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

    # Метод для подсчета количества узлов
    def count_nodes(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.l) + self._count_nodes(node.r)

    # Метод для подсчета количества листьев
    def count_leaves(self):
        return self._count_leaves(self.root)

    def _count_leaves(self, node):
        if node is None:
            return 0
        if node.l is None and node.r is None:
            return 1
        return self._count_leaves(node.l) + self._count_leaves(node.r)

    # Метод для вычисления высоты дерева
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.l), self._height(node.r))

    # Обход в глубину с использованием стека
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

    # Метод для красивого вывода дерева (горизонтальный вывод)
    def print_tree(self):
        if self.root is None:
            print("Дерево не существует")
            return

        def print_node(node, prefix="", is_left=True):
            if node is not None:
                print_node(node.r, prefix + ("│   " if is_left else "    "), False)
                print(prefix + ("└── " if is_left else "┌── ") + str(node.v))
                print_node(node.l, prefix + ("    " if is_left else "│   "), True)

        print("\nГоризонтальный вывод дерева:")
        print_node(self.root)


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
    bst.print_tree()