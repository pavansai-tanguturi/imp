import sys

NODES = 5
INF = sys.maxsize

def min_distance(dist, visited):
    min_val = INF
    min_index = -1
    for v in range(NODES):
        if not visited[v] and dist[v] < min_val:
            min_val = dist[v]
            min_index = v
    return min_index

def print_routing_table(dist, src):
    print(f"Routing table for node {src}:")
    for i in range(NODES):
        print(f"Node {i}: Distance {dist[i]}")
    print()

def ospf_routing(graph, src):
    dist = [INF] * NODES
    visited = [False] * NODES
    dist[src] = 0

    for _ in range(NODES - 1):
        u = min_distance(dist, visited)
        visited[u] = True

        for v in range(NODES):
            if not visited[v] and graph[u][v] and dist[u] != INF and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    print_routing_table(dist, src)

def main():
    graph = [
        [0, 10, INF, 30, 100],
        [10, 0, 50, INF, INF],
        [INF, 50, 0, 20, 10],
        [30, INF, 20, 0, 60],
        [100, INF, 10, 60, 0]
    ]

    for i in range(NODES):
        ospf_routing(graph, i)

if __name__ == "__main__":
    main()