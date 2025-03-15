total_sums = 0
def arraySum(A,start,end,i=1):
    global total_sums
    if start == end:
        print(f"Base Case Reached: A[{start},{end}] = {A[start]} returned")
        return A[start]
    else:
        mid = (start + end) // 2
        print(f"Split Array: Input Array = {A[start:end+1]} -> Output Arrays = {A[start:mid+1]} and {A[mid+1:end+1]}")
        left_half = arraySum(A,start,mid)
        right_half = arraySum(A,mid+1,end)
        sum_value = left_half + right_half
        total_sums += 1
        print(f"Sum: {left_half} + {right_half} = {sum_value} returned | Total Sums = {total_sums}")
        return sum_value


def main():
    global total_sums
    # Test Instance 1
    A = [38, 21, 39, 60, -1, 10, 81, 23]
    print(f"\nSum of Array: {arraySum(A,0,len(A)-1)} | Total Sums Executed: {total_sums}")

    # Test Instance 2
    print()
    print()
    total_sums = 0
    B = [2, 97, 5, 88, 9, 72, 12, 64, 17, 56, 21]
    print(f"\nSum of Array: {arraySum(B,0,len(B)-1)} | Total Sums Executed: {total_sums}")

    # Test Instance 3
    print()
    print()
    total_sums = 0
    C = [100, 33, 22, 213, 65, 29, 153, 199, 47, 181, 85]
    print(f"\nSum of Array: {arraySum(C,0,len(C)-1)} | Total Sums Executed: {total_sums}")


if __name__ == '__main__':
    main()
