class DHG:
    def __init__(self, first, second):
        self.arr1 = list(first)
        self.arr2 = list(second)
        self.flag = 0  # Checks if the intersection has occured or not
        self.result = 0  # Answer

    # Binary Search which returns the index of the matched value
    @staticmethod
    def _binary_search(start, end, lst, value): 
        while start <= end :
            mid = start + (end - start) // 2

            if lst[mid] == value: 
                return mid 
            elif lst[mid] < value: 
                start = mid + 1
            else: 
                end = mid - 1                
        return -1   

    # Returns the maximum sum possible
    def solve(self):
        arr1 = self.arr1[1:]
        arr2 = self.arr2[1:]
        prev_max_ind1 = 0  # Prefix array marker for previous intersection: arr1
        prev_max_ind2 = 0  # Prefix array marker for previous intersection: arr2

        # Prefix Array 1
        pa1 = []
        pa1.append(arr1[0])
        for index in range(1, self.arr1[0]):
            pa1.append(pa1[index - 1] + arr1[index])

        # Prefix Array 2
        pa2 = []
        pa2.append(arr2[0])
        for index in range(1, self.arr2[0]):
            pa2.append(pa2[index - 1] + arr2[index])

        for index in range(self.arr1[0]):
            # Stores the index of arr2 where intersection has occured
            bs_int = DHG._binary_search(
                prev_max_ind2, self.arr2[0] - 1, arr2, arr1[index]
            )

            if bs_int != -1:
                if self.flag == 0:
                    """ If there was no intersection previously,
                        then select the maximum of pa1[index] and pa2[bs_int] """
                    self.flag = 1
                    self.result += max(pa1[index], pa2[bs_int])
                else:
                    """ Else, find the maximum of the difference between the
                        prefix sum at current intersection and previous intersection """
                    self.result += max(
                        pa1[index] - pa1[prev_max_ind1], pa2[bs_int] - pa2[prev_max_ind2]
                    )

                prev_max_ind1 = index
                prev_max_ind2 = bs_int

        # If there was no intersection, find the maximum of prefix array of final indexes
        if self.flag == 0:
            self.result += max(pa1[self.arr1[0] - 1], pa2[self.arr2[0] - 1])

        # Else, find the maximum of the difference of prefix sum at final index and their last intersection
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
