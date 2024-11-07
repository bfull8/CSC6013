def BFS(V, E):
    for i in range(len(V)):
        V[i] = -1                                           # all vertices not visited
    count = 0
    for i in range(len(V)):                                 # for all possible sources
        if (V[i] == -1):
            Q = [i]                                         # enqueue the source
            print(f"Vertex {i} enqueued")
            print(f"Queue: {Q}")
            V[i], count = count, count+1                    # visit it
            print(f"Vertex {V[i]} visited")
            print(f"Array V: {V}")
            while (len(Q) != 0):                            # for all enqueued
                for e in E:                                 # search neighbors
                    if (e[0] == Q[0]) and (V[e[1]] == -1):
                        Q.append(e[1])                      # enqueue it
                        print(f"Vertex {e[1]} enqueued")
                        print(f"Queue: {Q}")
                        V[e[1]], count = count, count+1     # visit it
                        print(f"Vertex {e[1]} visited")
                        print(f"Array V: {V}")
                    elif (e[1] == Q[0]) and (V[e[0]] == -1):
                        Q.append(e[0])                      # enqueue it
                        print(f"Vertex {e[1]} enqueued")
                        print(f"Queue: {Q}")
                        V[e[0]], count = count, count+1     # visit it
                        print(f"Vertex {e[1]} visited")
                        print(f"Array V: {V}")
                print(f"Vertex {Q.pop(0)} dequeued")                                    # dequeue it
                print(f"Queue: {Q}")

V = [0]*9
E = [[0,1,1], [0,2,1], [0,3,1], [1,4,1], [3,6,1],
     [4,5,1], [4,7,1], [5,8,1], [7,8,1]]
BFS(V,E)
print(V)
