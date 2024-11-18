def DFS(V,E):
    def __visit(i, count):
        V[i], count = count, count + 1
        for e in E:
            if (e[0] == i and (V[e[1]]) == -1):
                print(f"Recursive call made for node {e[0]}")
                count = __visit(e[1],count)
            elif (e[1] == i) and (V[e[0]] == -1):
               count = __visit(e[0],count)
        return count

    for i in range(len(V)):
        V[i] = -1
    count = 0
    for i in range(len(V)):
        if (V[i] == -1):
            count = __visit(i,count)

V = [0]*9
E = [[0,1,1],[0,2,1],[0,3,1],[1,4,1],[3,6,1],
     [4,5,1],[4,7,1],[5,8,1],[7,8,1]]

V = [0]*8
E = [[0,4,1],[0,7,1],[1,0,1],[2,5,1],[2,6,1],[3,0,1],[3,4,1],
     [4,2,1],[5,3,1],[5,4,1],[6,1,1],[6,4,1],[7,3,1]]


DFS(V,E)
print(V)

# A 0
# B 1
# C 2
# D 3
# E 4
# F 5
# G 6
# H 7
