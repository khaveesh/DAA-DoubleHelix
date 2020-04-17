# coding=utf-8
"""Tests the solution."""
import unittest

import anarc05b_double_helix as dp
import anarc05b_double_helix_greedy as grdy


class Test(unittest.TestCase):
    """Unittest requires a class of TestCase to run."""

    def setUp(self) -> None:
        """Testcase class is setup to run tests."""
        in_lists = (
            (
                "13 3 5 7 9 20 25 30 40 55 56 57 60 62",
                "11 1 4 7 11 14 25 44 47 55 57 100",
                450,
            ),
            ("4 -5 100 1000 1005", "3 -12 1000 1001", 2100),
        )

        self.lists = (
            (
                tuple(map(int, iter_list[0].split())),
                tuple(map(int, iter_list[1].split())),
                iter_list[2],
            )
            for iter_list in in_lists
        )

    def test_double_helix_dp(self) -> None:
        """Function to test the dynamic programming solution using unittest framework."""
        for element in self.lists:
            with self.subTest(element):
                self.assertEqual(
                    dp.DoubleHelix(element[0], element[1]).solve(), element[2],
                )

    def test_double_helix_greedy(self) -> None:
        """Function to test the greedy solution using unittest framework."""
        for element in self.lists:
            with self.subTest(element):
                self.assertEqual(
                    grdy.DHG(element[0], element[1]).solve(), element[2],
                )


if __name__ == "__main__":
    unittest.main()
