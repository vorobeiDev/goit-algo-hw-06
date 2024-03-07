from collections import deque
from ex01 import G


def dfs_iterative(G, start_vertex, target_vertex):
    visited = set()
    stack = [(start_vertex, [start_vertex])]  # Стек містить кортежі (вершина, шлях до неї)

    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == target_vertex:
                return path  # Повертаємо шлях, як тільки знайшли ціль
            visited.add(vertex)
            for next_vertex in set(G.neighbors(vertex)) - visited:
                stack.append((next_vertex, path + [next_vertex]))


def bfs_iterative(G, start_vertex, target_vertex):
    visited = set()
    queue = deque([(start_vertex, [start_vertex])])  # Черга містить кортежі (вершина, шлях до неї)

    while queue:
        (vertex, path) = queue.popleft()
        if vertex not in visited:
            if vertex == target_vertex:
                return path  # Повертаємо шлях, як тільки знайшли ціль
            visited.add(vertex)
            for next_vertex in set(G.neighbors(vertex)) - visited:
                queue.append((next_vertex, path + [next_vertex]))


# Ваш граф транспортної мережі, як ви його визначили...

# Пошук маршруту DFS
dfs_path = dfs_iterative(G, "Боярка", "Північний")
print("DFS шлях:", dfs_path)

# Пошук маршруту BFS
bfs_path = bfs_iterative(G, "Боярка", "Північний")
print("BFS шлях:", bfs_path)