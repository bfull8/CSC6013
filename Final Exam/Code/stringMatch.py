def stringMatch(string,substr):
    for i in range(len(string)-len(substr) + 1):
        k = 0
        for j in range(len(substr)):
            if string[i+j] == substr[j]:
                k += 1
                continue
            else:
                break
        if k == len(substr):
            return i

def stringMatch2(S,R):
    for i in range(len(S)-len(R) + 1):
        j, k = i, 0
        while (k < len(R)) and (S[j] == R[k]):
            j += 1
            k += 1
        if k == len(R):
            return i

    return None


print(stringMatch('racecar','car'))
print(stringMatch2('racecar','car'))
