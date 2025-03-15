def closestPair(A):
    minDist, ans = float('inf'), []
    for i in range(len(A) - 1):
        dist = 0
        for j in range(i+1, len(A)):
            for k in range(len(A[i])):
                dist += (A[i][k] - A[j][k]) ** 2
            dist = dist ** 0.5

            if dist < minDist:
                minDist, pair = dist, [i,j]
    return pair[0], pair[1]

p = [[2,3],[-4,1],[0,-5],[6,0]]

i,j = closestPair(p)
print(p[i],p[j])
