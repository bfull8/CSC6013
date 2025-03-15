def BFS(E):
    V = []                                                  # Visited List
    vertices = set()                                        # Distinct set of vertices
    for e in E:
        vertices.add(e[0])
        vertices.add(e[1])

    for vertex in sorted(vertices):                                 # for all possible sources
        if vertex not in V:
            Q = [vertex]                                     # enqueue the source
            print(f"Vertex {vertex} enqueued, Queue: {Q}")
            V.append(vertex)                                # visit it
            print(f"Vertex {vertex} visited,  Visited: {V}")
            while (len(Q) != 0):                            # for all enqueued
                for e in E:                                 # search neighbors
                    if (e[0] == Q[0]) and (e[1] not in V):
                        Q.append(e[1])                      # enqueue it
                        print(f"Vertex {e[1]} enqueued, Queue: {Q}")
                        V.append(e[1])
                        print(f"Vertex {e[1]} visited,  Visited: {V}")
                print(f"Vertex {Q.pop(0)} dequeued, Queue: {Q}")                                    # dequeue it
    return V

E = [["A","B",1], ["A","D",1], ["B","A",1], ["B","C",1], ["B","G",1], ["C","A",1],
     ["C","B",1], ["D","E",1], ["D","F",1], ["E","F",1], ["F","B",1], ["G","C",1],
     ["G","F",1]]

V = BFS(E)
print("Visited Order: ")
for i, element in enumerate(V):
    print(f"{i+1}. {element}")
