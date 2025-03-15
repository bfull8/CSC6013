def arrayDiff(A,B):
    # Array to hold set difference
    C = []

    # For each element in A, check it against each element in B
    # If the number of differences = the length of B, it is not in B
    for a in A:
        count = 0
        for b in B:
            print(f"Array A element: {a} | Array B element {b}",end = " ")
            if a != b:
                print(" - Elements do not match. Increment Counter")
                count += 1
            else:
                break # break early if there is one match

        if count == len(B):
            C.append(a)
            print(f"{a} is not within B:{B}, adding to C | Array C = {C}")
        else:
            print(f" - {a} is within B:{B}")
        print()

    return C

A = [20, 40, 70, 30, 10, 80, 50, 90, 60]
B = [35, 45, 55, 60, 50, 40]
print(f"Final Array C: {arrayDiff(A,B)}")

for a in A:
    if a not in B:
        print(a)
