# coding=utf-8
"""Solves the ANARC05B problem in SPOJ."""
import cProfile


class DoubleHelix:
    """Class to solve the double helix problem."""

    def __init__(self, first, second) -> None:
        """Class variables are initialized with the input values.

        Args:
            first: The first array
            second: The second array
        """
        self.first = list(first)
        self.second = list(second)
        self.iter_first: int = 1
        self.iter_second: int = 1

    def solve(self) -> int:
        """Solves the double helix for the given input arrays.

        Returns:
            The maximum sum possible.
        """
        length = (self.first[0], self.second[0])
        self.first[0] = 0
        self.second[0] = 0

        while self.iter_first <= length[0] and self.iter_second <= length[1]:
            self._solve_helper()

        while self.iter_first <= length[0]:
            self._inc_first()
        while self.iter_second <= length[1]:
            self._inc_second()

        return max(self.first[-1], self.second[-1])

    def _solve_helper(self) -> None:
        if self.first[self.iter_first] < self.second[self.iter_second]:
            self._inc_first()
        elif self.first[self.iter_first] > self.second[self.iter_second]:
            self._inc_second()
        else:  # Intersection Point
            self._inc_first()
            self._inc_second()
            self._assign_max()

    def _assign_max(self) -> None:
        val_first, val_second = self.iter_first - 1, self.iter_second - 1
        if self.first[val_first] > self.second[val_second]:
            self.second[val_second] = self.first[val_first]
        else:
            self.first[val_first] = self.second[val_second]

    def _inc_first(self) -> None:
        self.first[self.iter_first] += self.first[self.iter_first - 1]
        self.iter_first += 1

    def _inc_second(self) -> None:
        self.second[self.iter_second] += self.second[self.iter_second - 1]
        self.iter_second += 1


if __name__ == "__main__":
    while True:
        FIRST = input()
        if FIRST[0] == "0":
            break
        # Convert string input to list of ints
        SECOND = map(int, input().split())
        # Create an instance of the class and call solve function
        cProfile.run("print(DoubleHelix(map(int, FIRST.split()), SECOND).solve())")
