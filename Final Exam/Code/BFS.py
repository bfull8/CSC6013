def BFS(V,E):
    for i in range(len(V)):
        V[i] = -1

    count = 0
    for i in range(len(V)):
        if V[i] == -1:
            Q = [i]
            V[i], count = count, count + 1
            while len(Q) != 0:
                for e in E:
                    if (E[0] == Q[0]) and (V[e[1]] == -1):
                        Q.append(e[1])
                        V[e[1]], count = count, count + 1
                    elif (E[1] == Q[0]) and (V[e[0]] == -1):
                        Q.append(e[0])
                        V[e[0]], count = count, count + 1
                Q.pop(0)

V = [0]*9

E = [[0,1,1],[0,2,1],[0,3,1],[1,4,1],[3,6,1],[4,5,1],[4,7,1],[5,8,1],[7,8,1]]
BFS(V,E)
print(V)
