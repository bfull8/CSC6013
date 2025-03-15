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

    return visited

E = [["A","B",1], ["A","D",1], ["B","A",1], ["B","C",1], ["B","G",1], ["C","A",1],
     ["C","B",1], ["D","E",1], ["D","F",1], ["E","F",1], ["F","B",1], ["G","C",1],
     ["G","F",1]]



V = DFS(E)
print("Visited Order: ")
for i, element in enumerate(V):
    print(f"{i+1}. {element}")
