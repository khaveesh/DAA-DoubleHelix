# coding=utf-8
"""Tests the solution."""
import unittest

import anarc05b_double_helix as dp
import anarc05b_double_helix_greedy as grdy


class Test(unittest.TestCase):
    """Unittest requires a class of TestCase to run."""

    def setUp(self) -> None:
        """Testcase class is setup to run tests."""
        with open("testcases.txt") as file_desc:
            inp = tuple(filter(None, file_desc.read().splitlines()))
            temp_list = (inp[index : index + 3] for index in range(0, len(inp), 3))
            self.lists = (
                (
                    tuple(map(int, iter_list[0].split())),
                    tuple(map(int, iter_list[1].split())),
                    int(iter_list[2]),
                )
                for iter_list in temp_list
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
