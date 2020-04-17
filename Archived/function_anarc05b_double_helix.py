# coding=utf-8
"""Solves the ANARC05B problem in SPOJ."""


def solve_double_helix(first, second) -> int:
    """Solves the double helix for the given input arrays.

    Args:
        first: The first array.
        second: The second array.

    Returns:
        The maximum sum possible.
    """
    length = (first[0], second[0])
    first[0] = 0
    second[0] = 0
    iter_first, iter_second = 1, 1

    while iter_first <= length[0] and iter_second <= length[1]:
        if first[iter_first] < second[iter_second]:
            first[iter_first] += first[iter_first - 1]
            iter_first += 1
        elif first[iter_first] > second[iter_second]:
            second[iter_second] += second[iter_second - 1]
            iter_second += 1
        else:
            first[iter_first] += first[iter_first - 1]
            second[iter_second] += second[iter_second - 1]
            if first[iter_first] > second[iter_second]:
                second[iter_second] = first[iter_first]
            else:
                first[iter_first] = second[iter_second]
            iter_first += 1
            iter_second += 1

    while iter_first <= length[0]:
        first[iter_first] += first[iter_first - 1]
        iter_first += 1
    while iter_second <= length[1]:
        second[iter_second] += second[iter_second - 1]
        iter_second += 1
    return max(first[length[0]], second[length[1]])


if __name__ == "__main__":
    while True:
        FIRST = list(map(int, input().split()))
        if FIRST[0] == 0:
            break
        SECOND = list(map(int, input().split()))
        print(solve_double_helix(FIRST, SECOND))
