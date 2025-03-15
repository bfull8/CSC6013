map = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}

def DFS(E):
    visited = []
    def __visit(vertex, count):
        print(f"DFS called for vertex {vertex}")
        visited.append(vertex)
        print(f"Vertex {vertex} is visited and received the stamp {count} | Visited: {visited}")
        count = count + 1                                # Visit the node
        for e in E:
            if (e[0] == vertex) and (e[1] not in visited):     # Vist each of the neighbors for the node
                count = __visit(e[1],count)
        return count

    vertices = set()
    for e in E:
        vertices.add(e[0])
        vertices.add(e[1])

    count = 0
    for vertex in sorted(vertices):
        if vertex not in visited:
            count = __visit(vertex,count)

E = [["A","E",1],["A","H",1],["B","A",1],["C","F",1],["C","G",1],
     ["D","A",1],["D","E",1],["E","C",1],["F","D",1],["F","E",1],
     ["G","B",1],["G","E",1],["H","D",1]]


DFS(E)
