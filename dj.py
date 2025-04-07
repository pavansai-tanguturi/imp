N = 5
I = 99999

# Function to find the vertex with the minimum distance that hasn't been visited
def m(d, v):
    x = I
    p = -1
    for i in range(N):
        if not v[i] and d[i] < x:
            x = d[i]
            p = i
    return p

# Function to compute the routing table for a given source node
def o(g, s):
    d = [I] * N
    v = [0] * N
    d[s] = 0
    
    for i in range(N - 1):
        u = m(d, v)  # Find the node with the minimum distance
        v[u] = 1  # Mark the node as visited
        
        for j in range(N):
            if not v[j] and g[u][j] and d[u] + g[u][j] < d[j]:
                d[j] = d[u] + g[u][j]  # Update the distance to node j
    
    print(f"Routing Table for Node {s}:")
    for i in range(N):
        print(f"To {i}: Cost = {d[i]}")

# Main function to run the Dijkstra's algorithm for each node
def main():
    g = [
        [0, 10, I, 30, 100],
        [10, 0, 50, I, I],
        [I, 50, 0, 20, 10],
        [30, I, 20, 0, 60],
        [100, I, 10, 60, 0]
    ]
    
    for i in range(N):
        o(g, i)

# Run the main function
if __name__ == "__main__":
    main()