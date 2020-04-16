"""Algorithm : Take the input arrays, make a prefix array and
               then binary search for the intersection points
               and then greedily select the maximum of the intersection
               from respective prefix arrays
"""


class DHG:
    def __init__(self, first, second):
        self.arr1 = first
        self.arr2 = second
        self.flag = 0  # Checks if the intersection has occured or not
        self.result = 0  # Answer

    # Binary Search
    @staticmethod
    def binary_search(start, end, lst, val):
        if end < start:
            return -1
        else:
            mid = start + (end - start) // 2

            if lst[mid] == val:
                return mid
            elif lst[mid] < val:
                return DHG.binary_search(mid + 1, end, lst, val)
            else:
                return DHG.binary_search(start, mid - 1, lst, val)

    def solve(self):
        arr1 = self.arr1[1:]
        arr2 = self.arr2[1:]
        prev_max_ind1 = 0  # Prefix array marker for previous intersection: arr1
        prev_max_ind2 = 0  # Prefix array marker for previous intersection: arr2

        # Prefix Array 1
        pa1 = []
        pa1.append(arr1[0])
        for i in range(1, self.arr1[0]):
            pa1.append(pa1[i - 1] + arr1[i])

        # Prefix Array 2
        pa2 = []
        pa2.append(arr2[0])
        for i in range(1, self.arr2[0]):
            pa2.append(pa2[i - 1] + arr2[i])

        for i in range(self.arr1[0]):
            # Checks for the intersection point
            bs_val = DHG.binary_search(prev_max_ind2, self.arr2[0] - 1, arr2, arr1[i])

            if bs_val != -1:
                if self.flag == 0:
                    self.flag = 1
                    self.result += max(pa1[i], pa2[bs_val])
                else:
                    self.result += max(
                        pa1[i] - pa1[prev_max_ind1], pa2[bs_val] - pa2[prev_max_ind2]
                    )

                prev_max_ind1 = i
                prev_max_ind2 = bs_val

        if self.flag == 0:
            self.result += max(pa1[self.arr1[0] - 1], pa2[self.arr2[0] - 1])

        else:
            self.result += max(
                pa1[self.arr1[0] - 1] - pa1[prev_max_ind1],
                pa2[self.arr2[0] - 1] - pa2[prev_max_ind2],
            )

        return self.result


if __name__ == "__main__":
    while True:
        a1 = list(map(int, input().split()))
        if a1[0] == 0:
            break
        a2 = list(map(int, input().split()))
        print(DHG(a1, a2).solve())
