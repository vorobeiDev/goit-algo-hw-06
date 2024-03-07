import heapq
from ex01 import G


def dijkstra(G, start):
    distances = {vertex: float('infinity') for vertex in G.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in G.neighbors(current_vertex):
            weight = G[current_vertex][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == '__main__':
    start_vertex = "Боярка"
    distances = dijkstra(G, start_vertex)
    print(f"Найкоротші шляхи від {start_vertex} до всіх інших вершин:")
    for vertex, distance in distances.items():
        print(f"До {vertex}: {distance} хвилин")