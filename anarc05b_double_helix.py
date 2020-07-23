"""Author - Khaveesh N IMT2018036. Solves the ANARC05B problem in SPOJ."""

import typing
from dataclasses import dataclass


@dataclass
class DoubleHelix:
    """Class to solve the double helix problem."""

    first: typing.List[int]
    second: typing.List[int]

    iter_first = 0
    iter_second = 0

    sum1 = 0
    sum2 = 0

    def solve(self) -> int:
        """Solves the double helix for the given input arrays.

        Returns:
            The maximum sum possible.
        """
        length: typing.Tuple[int, int] = (self.first.pop(0), self.second.pop(0))

        while self.iter_first < length[0] and self.iter_second < length[1]:
            self._solve_helper()

        while self.iter_first < length[0]:
            self._inc_first()
        while self.iter_second < length[1]:
            self._inc_second()

        return max(self.sum1, self.sum2)

    def _solve_helper(self) -> None:
        if self.first[self.iter_first] < self.second[self.iter_second]:
            self._inc_first()
        elif self.first[self.iter_first] > self.second[self.iter_second]:
            self._inc_second()
        else:  # Intersection Point
            self._inc_first()
            self._inc_second()
            # Assigning the maximum of sum1 & sum2 to both
            if self.sum1 > self.sum2:
                self.sum2 = self.sum1
            else:
                self.sum1 = self.sum2

    def _inc_first(self) -> None:
        self.sum1 += self.first[self.iter_first]
        self.iter_first += 1

    def _inc_second(self) -> None:
        self.sum2 += self.second[self.iter_second]
        self.iter_second += 1


if __name__ == "__main__":
    while True:
        # Convert string input to list of ints
        FIRST: typing.List[int] = list(map(int, input().split()))
        if FIRST[0] == 0:  # End condition
            break
        SECOND: typing.List[int] = list(map(int, input().split()))

        # Create an instance of the class and call solve function
        print(DoubleHelix(FIRST, SECOND).solve())
