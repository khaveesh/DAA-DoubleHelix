"""Algorithm : Take the input arrays, make a prefix array and
               then binary search for the intersection points
               and then greedily select the maximum of the intersection
               from respective prefix arrays
"""

# Binary Search
def binary_search(start, end, lst, val):
    if end < start:
        return -1
    else:
        mid = start + (end - start) // 2

        if lst[mid] == val:
            return mid
        elif lst[mid] < val:
            return binary_search(mid + 1, end, lst, val)
        else:
            return binary_search(start, mid - 1, lst, val)


def solve(arr1, arr2):
    la1 = arr1[0]  # Length of arr1
    la2 = arr2[0]  # Length of arr2
    arr1 = arr1[1:]
    arr2 = arr2[1:]
    pa1 = []  # Prefix Sum Array of A1
    pa2 = []  # Prefix Sum Array of A2
    pa1.append(arr1[0])
    pa2.append(arr2[0])
    result = 0  # Answer
    prev_max_ind1 = 0  # Prefix array marker for previous intersection: arr1
    prev_max_ind2 = 0  # Prefix array marker for previous intersection: arr2
    flag = 0  # Checks if the intersection has occured or not

    # Prefix Array 1
    for i in range(1, la1):
        pa1.append(pa1[i - 1] + arr1[i])

    # Prefix Array 2
    for i in range(1, la2):
        pa2.append(pa2[i - 1] + arr2[i])

    for i in range(la1):
        # Checks for the intersection point
        bs_val = binary_search(prev_max_ind2, la2 - 1, arr2, arr1[i])

        if bs_val != -1:
            if flag == 0:
                flag = 1
                result += max(pa1[i], pa2[bs_val])
            else:
                result += max(
                    pa1[i] - pa1[prev_max_ind1], pa2[bs_val] - pa2[prev_max_ind2]
                )

            prev_max_ind1 = i
            prev_max_ind2 = bs_val

    if flag == 0:
        result += max(pa1[la1 - 1], pa2[la2 - 1])

    else:
        result += max(
            pa1[la1 - 1] - pa1[prev_max_ind1], pa2[la2 - 1] - pa2[prev_max_ind2]
        )

    return result


if __name__ == "__main__":
    while True:
        arr1 = list(map(int, input().split()))
        if arr1[0] == 0:
            break
        arr2 = list(map(int, input().split()))
        print(solve(arr1, arr2))
